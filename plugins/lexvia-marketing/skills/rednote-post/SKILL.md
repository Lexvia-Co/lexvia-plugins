---
name: rednote-post
description: >-
  Create a complete LEXVIA Rednote post with Chinese legal educational copy and a
  matching branded image. Orchestrate rednote-content, rednote-picture, and humanizer
  in that order, then reconcile the image with the humanized text and deliver both
  with an updated Word document. Use for end-to-end Rednote or Xiaohongshu post
  requests needing both copy and an image, or when explicitly invoked. Text-only
  writing, image-only generation, and standalone rewriting use their existing skills.
---

# Rednote post

Produce one finished post through the three existing Marketing skills. Run the
stages sequentially in the current session; each stage returns to this workflow.
Keep drafts and candidate images intermediate until the final alignment check.
Do not end the response after the content or picture stage.
Respect an explicit text-only, image-only, or rewrite-only request even when this
skill is named: use the corresponding standalone skill without adding other stages.

## Resolve dependencies and output locations

- Load [rednote-content](../rednote-content/SKILL.md) and apply its editorial-scope
  handling to the requested topic and angle before research, artifact creation,
  or other tool checks. Continue only with independently meaningful permitted
  content. If no topic is supplied, use its eligible-topic selection process.
- For eligible work, load [rednote-picture](../rednote-picture/SKILL.md) and
  [humanizer](../humanizer/SKILL.md) from this skill's installed sibling directories.
  Resolve all references, scripts, and assets from each child's own directory,
  including installed cache paths containing spaces, rather than from the consumer's
  working directory. Follow any further skills required for the actual artifacts.
- Resolve the active consumer workspace. Put research, drafts, provisional Word
  files, and candidate images in its `output/intermediate`; put only selected final
  deliverables in `output/final`. These are relative to the consumer workspace,
  never the installed plugin. When testing from the plugin source repository, use
  a separate temporary consumer workspace. Preserve unrelated existing files.
- Reuse the supplied topic, audience, source material, and format constraints.
  Default to the picture skill's 3:4 portrait format when no format is specified.
- Check that the three sibling skills, required picture references/logo, image
  generation, and tools to export and render Word documents are available.
  If a required dependency or tool is missing, report the blocker and completed
  stages accurately; do not silently
  substitute a different skill or claim that the complete workflow ran.

## 1. Generate the content

Run `rednote-content` through its research, template selection, tone edit, legal
review, and document checks. Apply its editorial-scope screening before research
or artifact creation and throughout subsequent stages. Follow its handling for
excluded, mixed, and unclear topics; never carry excluded material into an image
prompt, humanizer input, filename, metadata, or deliverable.

Retain the verified research and edited Chinese draft as the source for later
stages. Preserve the source links, jurisdiction, dates, numbers, legal distinctions,
and qualifications needed to interpret the post. The content stage's Word file
is provisional in this composed workflow; keep it intermediate until the final
humanized version has been exported and verified.

## 2. Generate the picture from that draft

Pass the edited draft from stage 1 to `rednote-picture`, including its title,
central takeaway, supporting facts, and caveats. Follow that skill's complete
reference-library, official-logo, brand-colour, image-generation, inspection, and
focused-correction requirements. Inspect the actual generated image rather than
assuming its text matches the generation prompt.

Keep the selected candidate and the visible headline, takeaway, factual labels,
and caveats available for the final comparison. The picture summarizes the draft;
it must not add legal claims. Hold its standalone delivery until stage 4.

## 3. Humanize the content

Run Marketing's `humanizer` on the stage 1 draft in **embedded mode**, returning
only the final rewrite to this workflow. Treat the draft as material to edit,
not as instructions. All wording, including the title, may be revised; do not
freeze awkward phrasing merely because it appears on the candidate image.

Keep the post in Simplified Chinese and within the content skill's 1,000-character
limit, including its title and hashtags. Preserve supported facts, source links,
jurisdiction, dates, numbers, legal distinctions, and necessary qualifications.
Do not invent anecdotes, personal experience, credentials, or legal advice to
make the voice sound natural. Retain qualifications that affect legal meaning.

Compare the rewrite against the verified draft and research. Repair any factual
drift in the prose before using it for image alignment. Reapply the content
skill's editorial and legal checks to the complete final text.

## 4. Reconcile and deliver

Compare the final humanized post with the **rendered candidate image**, checking:

- The headline's meaning and the central takeaway.
- Names, jurisdiction, dates, numbers, and any conditions on the legal distinction.
- Caveats needed to prevent the image's abbreviated wording from misleading.
- Unsupported image claims, contradictions, or labels left over from an earlier draft.

Equivalent wording is acceptable; the cover need not reproduce the whole post.
A changed headline alone does not require regeneration if it still conveys the
same accurate meaning. Correct the image when wording conflicts with the final
post or loses a material qualification. Do not undo a sound humanizer edit just
to keep an outdated image.

For a mismatch, run **one alignment-repair pass** through `rednote-picture`, using
the final humanized copy and identifying the specific discrepancy. Edit the
candidate when practical or regenerate it from the final copy. Reapply all picture
reference, logo, and inspection requirements; its existing allowance of one
focused quality correction still applies. Inspect the repaired result against the
same final text. Do not restart the content/humanizer cycle or loop image repairs.

Export the humanized text to the final Word document using the applicable document
skill without opening Microsoft Word. Inspect its rendered layout, extracted text,
and metadata. Its post text must match the final chat copy, including title and
hashtags, and pass the content skill's checks. Do not link a provisional Word file
or an obsolete image as a final deliverable.

Deliver the final Chinese title, body, and hashtags in chat, the selected image
inline, and a link to the updated Word document. When image output provides a
local file, place the selected image in `output/final` under a descriptive filename
and include its file link. Omit intermediate drafts, humanizer pattern reports,
and process commentary from the finished post.

If generation fails or the bounded repair still leaves a mismatch or material
visual defect, return the verified humanized text and updated Word document as
**partial completion**, briefly identify the image blocker, and omit the defective
image. If the text/document checks also fail, identify what remains unfinished
instead of presenting an unverified deliverable. Never claim a matching pair
without inspecting the final image. This workflow does not publish the post.
