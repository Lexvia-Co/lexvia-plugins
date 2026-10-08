---
name: org-chart
description: Generate organization charts with personnel information and hierarchy structures in a predefined chart format. Use when asked to generate organization charts.
---

# Generating Organization Chart

## Required Information
- hierarchy information that shows an organization's personnel relationships such as supervisors, direct reports, and assistants. 

## Workflow
1. Obtain hierarchy information from the user and check if the information needs to be modified to match the hierarchy information template in `assets/hierarchy_template.md`. Conduct any modification necessary according to the template file. Output the modified hierarchy information in .txt format as an intermediate file. 

2. (optional) If the user supplies additional personnel information such as status, names, and titles, extract the information and reformat it according to the personnel information template in `assets/personnel_info_template.md`. Output the generate personnel information in .txt format as an intermediate file.

3. Use the formatted hierarchy information from step 1 and personnel information from step 2, if any, to generate a clean tab-indented SmartArt Text Pane outline. The outline should preserve the supplied role hierarchy, note any assistant relationship, and include all information for each individual. 
Output the generate outline in .txt format as an intermediate file.

Example Text Pane Outline
---
Shenglan Ye | Chief Executive Officer | Citizenship Unknown
	Hang Ye | Senior Product Manager | Citizenship Unknown
		Chenxue Li | Product Manager | Citizen
			Baoyi Li | Administrator | PR 
			James Li | Interior Designer | Citizen
			Ting Yang | Accountant | Non PR
			Fu | Architect | Non PR 
Bei He | Chief Financial Officer | Citizen
	Yixiu Fu | Sales Manager | Citizen
		Yang He | Assistant Manager | Citizen

4. Generate a Microsoft SmartArt Org Chart with the text pane outline from step 3 with the Presentations plugin published by OpenAI. Installed first if the plugin is not already installed. The chart must follow the format rules in `references/smartart_display_format.md`. Output the .pptx file as an intermediate file. See `examples/example_org_chart.pptx` for example org chart. 

5. Copy and paste the chart generated in step 4 to a Word document according to the workflow in this file `references/pptx2word.md`. Save the document as an intermediate file. 

6. Resize the chart from step 5 according to the workflow in this file `references/chart_rescale.md`. Save the document as a final artifact. 

## Temp and output conventions
- Use `tmp/intermediate/` for intermediate files
- Write final artifacts under `output/`
- Keep filenames stable and descriptive.
- Use `tmp/code/` for any code files generated during the workflow

## Quality Checks
- Every text box in the org chart must be connected to another text box.
- For each text box, all text must fall within the boundary of each box. 
- For each text box, all text in the box must be displayed not be cut off or truncated.
- There must be no overlap between each text box in the chart. 
- Check that the final artifact is a valid Word document and can be opened in Microsoft Word without errors.

## Constraints
- Never use LibreOffice tools
- Never invoke user interface tools such as Microsoft PowerPoint or Microsoft Word. 

