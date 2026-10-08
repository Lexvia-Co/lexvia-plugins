PPTX2WORD
Purpose
---
Copy and paste a chart in a Powerpoint file to an editable chart in Word document.

Required Information
---
- a Microsoft PowerPoint file with an editable chart

Tool Constraints
---
- only use Documents plugin published by OpenAI. 
- Never use any user interface tools such as Microsoft Word. 

Workflow
---
1. Inspect the .pptx to confirm the org chart is native SmartArt or editable PowerPoint shapes, rather than a screenshot.

2. Select the complete chart in PowerPoint and copy it.

3. Create a blank Word document and change the orientation of the document to Landscape.

4. Paste using an Office-editable paste option, retaining SmartArt or grouped shapes where Word supports it. Check `examples/good_example_org_chart_doc.pdf` for an example of good rendering
and `examples/bad_example_org_chart_doc.docx` for the bad example. 

5. Check editability in Word by selecting the chart and confirming its text, shapes, and connectors can be changed. If it pastes as an image, rebuild it from the PowerPoint outline rather than scaling the image.

6. Inspect and modify the chart according to the formatting rules in `references/smartart_display_format.md`. 

7. Save as a new .docx in the chosen destination, without overwriting an existing file.

8. Check that the Word document is valid and can be opened in Microsoft Word without errors. If not inpsect the XML file and fix any error. 

