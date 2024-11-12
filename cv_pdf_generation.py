#!pip install reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

data = {
    'full-name' : 'John Smith',
    'mobile-number' : '12345678900',
    'email': 'johnsmith@data.com',
    'profile' : 'I am a hard worker with a range of skills',
    'Skills' : 'Communication, Coding',
    'Job title 1' : 'Data analyst',
    'Company 1': 'Rockborne',
    'Job 1 dates': ['Jun 2024', 'Present'],
    'Job 1 Description': 'I analysed some data projects',
    'project 1': 'Aviation Excel Dashboard',
    'project desc 1' : 'This is the project description',
    'Education 1': 'Rockborne Bootcamp',
    'Education School 1' : 'Rockborne',
    'Education Desc 1' : 'Learnt various skills',
    'Certificate 1': 'Snowflake Badge 1',
    'Certificate Date 1': 'Oct 2024'
}

def write_center(pdf, text : str, y_pos : float):
  """Adds the title to the PDF at the specified position.

  Args:
    pdf: The PDF canvas object.
    data: The dictionary containing the data.
    y_pos: The y-position for the title.

  """

  # Get the width of the full name text
  half_txt_width = pdf.stringWidth(text) / 2

  # Calculate the center position based on page width and text width
  center_x = (inch * 7 - half_txt_width) / 2

  # Add the title
  pdf.drawString(center_x, y_pos, text)

  print('Creating pdf...')
# Create a new PDF document
pdf = canvas.Canvas('prototype_cv.pdf')

page_width = 8.3*inch
page_len = 11.7*inch
pdf.setPageSize([page_width, page_len])

current_line = 11*inch
new_line = -0.3 * inch
new_line_s = -0.2 * inch
new_section = -0.6 * inch
margin_start = 0.5 * inch
# page_width = pdf.pagesize[0] / inch
margin_end = page_width - 0.5*inch
indent = '    '

def draw_divider(pdf, line):
    underline =  line + -0.1*inch
    pdf.line(margin_start, underline, margin_end, underline)

# Set font and font size
pdf.setFont("Helvetica", 12)

# write_center(pdf, data['full-name'].upper(), 11*inch)

pdf.drawCentredString(300, current_line, data['full-name'].upper())

current_line += new_line

## SUBTITLE ##
subtitle = data['mobile-number'] + ' • ' + data['email']
pdf.drawCentredString(300, current_line, subtitle)

### PROFILE ###
current_line += new_section
pdf.drawString(margin_start, current_line, data['profile'])


### SKILLS ###
current_line += new_section
pdf.drawString(margin_start, current_line, "SKILLS")
draw_divider(pdf, current_line)
current_line += new_line

pdf.drawString(margin_start, current_line, data['Skills'])

### WORK EXPERIENCE ###
current_line += new_section
pdf.drawString(margin_start, current_line, "WORK EXPERIENCE")
draw_divider(pdf, current_line)
current_line += new_line

pdf.drawString(margin_start, current_line, data['Job title 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, data['Company 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, data['Job 1 dates'][0] + " - " + data['Job 1 dates'][1])
current_line += new_line_s
pdf.drawString(margin_start, current_line, indent+data['Job 1 Description'])

### PROJECTS ###
current_line += new_section
pdf.drawString(margin_start, current_line, "PROJECTS")
draw_divider(pdf, current_line)
current_line += new_line

pdf.drawString(margin_start, current_line, data['project 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, indent+data['project desc 1'])

### EDUCATION ###
current_line += new_section
pdf.drawString(margin_start, current_line, "EDUCATION")
draw_divider(pdf, current_line)

current_line += new_line
pdf.drawString(margin_start, current_line, data['Education 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, data['Education School 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, indent+data['Education Desc 1'])

### CERTIFICATIONS ###
current_line += new_section
pdf.drawString(margin_start, current_line, "CERTIFICATIONS")
draw_divider(pdf, current_line)

current_line += new_line
pdf.drawString(margin_start, current_line, data['Certificate 1'])
current_line += new_line_s
pdf.drawString(margin_start, current_line, data['Certificate Date 1'])


# Save the PDF
pdf.save()

print('pdf ready')