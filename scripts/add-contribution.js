// Turns a workshop-contribution issue into:
//   1. workshops/<slug>/index.html, generated from scripts/workshop-template
//   2. a card entry in the LABS list of Agent-Studio-201/hub.html
// Usage: node scripts/add-contribution.js <issue-body-file> <issue-number>
const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const [bodyFile, issueNumber] = process.argv.slice(2);
const body = fs.readFileSync(bodyFile, "utf8");

// GitHub issue forms render each field as "### Label" followed by its value.
function field(label) {
  const re = new RegExp("### " + label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\s*\\n+([\\s\\S]*?)(?=\\n### |$)");
  const m = body.match(re);
  const v = m ? m[1].trim() : "";
  return v === "_No response_" ? "" : v;
}
function checked(label) {
  const v = field(label);
  return v ? v.split("\n").filter(l => l.includes("- [x]")).map(l => l.replace(/- \[x\]\s*/, "").trim()) : [];
}
const esc = s => s.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\r?\n/g, " ");
const html = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

const title = field("Content title");
const type = field("Content type");
const level = field("Level");
const team = field("Region / team");
const outcome = field("What does the attendee build?");
const duration = field("Duration (minutes)");
const link = field("Link to content");
const products = checked("Products used");

if (!title || !link || !outcome) {
  console.error("Missing required fields: title, link or outcome");
  process.exit(1);
}

// Same check the hub shows after submit; the submitter runs it in their own Glean.
function gleanPrompt() {
  return "Review this workshop I am submitting to the One PSA hub (a public GitHub Pages site).\n\n"
    + "Title: " + title + "\nLink: " + link + "\nProducts: " + (products.join(", ") || "not set") + "\nOutcome: " + outcome + "\n\n"
    + "1. Open the link. Can Docusign employees view it?\n"
    + "2. Search for existing workshops or labs that cover the same thing. List any with links.\n"
    + "3. Does the content actually use the products listed?\n"
    + "4. Flag any customer names, internal-only data, credentials or confidential material, since the hub is public.\n"
    + "5. Check it against our standard: prerequisites, copyable blocks, test inputs, guardrails, screenshots, recap. Which are missing?\n\n"
    + "Reply with pass or flag for each, with one line of reason.";
}

// 1. Generate the workshop page.
const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60) || "contribution-" + issueNumber;
const dir = path.join(root, "workshops", slug);
if (fs.existsSync(dir)) throw new Error("workshops/" + slug + " already exists");
const productPills = (products.length ? products : ["Other"]).map(p => `<span class="pill">${html(p)}</span>`).join("\n    ");
const page = fs.readFileSync(path.join(__dirname, "workshop-template", "index.html"), "utf8")
  .replace(/{{TITLE}}/g, html(title))
  .replace(/{{KICKER}}/g, html([type, level.split(" ")[0]].filter(Boolean).join(" · ")))
  .replace(/{{TEAM}}/g, html(team || "PSA"))
  .replace(/{{OUTCOME}}/g, html(outcome))
  .replace(/{{PRODUCTS}}/g, productPills)
  .replace(/{{DURATION}}/g, duration ? html(duration) + " min" : "Duration tbc")
  .replace(/{{LINK}}/g, html(link))
  .replace(/{{GLEAN_PROMPT}}/g, html(gleanPrompt()));
fs.mkdirSync(dir, { recursive: true });
fs.writeFileSync(path.join(dir, "index.html"), page);

// 2. Add the card to the hub. Lab entries end without a comma, so add one to the last.
const hubPath = path.join(root, "Agent-Studio-201", "hub.html");
const hub = fs.readFileSync(hubPath, "utf8");
const anchor = "// ----------------------------------------------------------------------------";
const idx = hub.indexOf(anchor);
if (idx === -1) throw new Error("LABS end marker not found in hub.html");
const closeIdx = hub.lastIndexOf("];", idx);
const entry = `  {tag:"${esc(type)}", icon:"route", title:"${esc(title)}", desc:"${esc(outcome)}", href:"../workshops/${slug}/index.html", meta:"${[duration ? duration + " min" : "Duration tbc", esc(level.split(" ")[0])].filter(Boolean).join(" · ")}", prods:${JSON.stringify(products.length ? products : ["Other"])}}`;
const before = hub.slice(0, closeIdx).replace(/\}\s*$/, "},");
fs.writeFileSync(hubPath, before + "\n" + entry + "\n" + hub.slice(closeIdx));

console.log(`Created workshops/${slug}/index.html and added hub card for #${issueNumber}`);
// Pass the slug to the workflow so it can link the submitter to their page.
if (process.env.GITHUB_OUTPUT) fs.appendFileSync(process.env.GITHUB_OUTPUT, "slug=" + slug + "\n");
