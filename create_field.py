from PIL import Image, ImageDraw

field_length = 900
field_width = 600
goal_width = 260
goal_area_width = 300
goal_area_length = 100
penalty_mark_dist = 150
center_circle_dia = 150
border_strip_with = 100
penalty_area_length = 200
penalty_area_width = 500

png_size = (field_length+border_strip_with*2,field_width+border_strip_with*2)
field_color = (0,150,0)
line_color = (255,255,255)

im = Image.new('RGB', png_size, field_color)
draw = ImageDraw.Draw(im)

draw.line((border_strip_with, border_strip_with,\
        border_strip_with+field_length, border_strip_with),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with+field_width,\
        border_strip_with+field_length, border_strip_with+field_width),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with,\
        border_strip_with, border_strip_with+field_width),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length, border_strip_with,\
        border_strip_with+field_length, border_strip_with+field_width),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length/2, border_strip_with,\
        border_strip_with+field_length/2, border_strip_with+field_width),\
        fill=line_color, width=6)
draw.line((border_strip_with+penalty_area_length, border_strip_with+field_width/2-penalty_area_width/2,\
        border_strip_with+penalty_area_length, border_strip_with+field_width/2+penalty_area_width/2),\
        fill=line_color, width=6)

draw.line((border_strip_with+field_length-penalty_area_length, border_strip_with+field_width/2-penalty_area_width/2,\
        border_strip_with+field_length-penalty_area_length, border_strip_with+field_width/2+penalty_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-penalty_area_length, border_strip_with+field_width/2-penalty_area_width/2,\
        border_strip_with+field_length, border_strip_with+field_width/2-penalty_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-penalty_area_length, border_strip_with+field_width/2+penalty_area_width/2,\
        border_strip_with+field_length, border_strip_with+field_width/2+penalty_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with+field_width/2+penalty_area_width/2,\
        border_strip_with+penalty_area_length, border_strip_with+field_width/2+penalty_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with+field_width/2-penalty_area_width/2,\
        border_strip_with+penalty_area_length, border_strip_with+field_width/2-penalty_area_width/2),\
        fill=line_color, width=6)

draw.line((border_strip_with+goal_area_length, border_strip_with+field_width/2-goal_area_width/2,\
        border_strip_with+goal_area_length, border_strip_with+field_width/2+goal_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-goal_area_length, border_strip_with+field_width/2-goal_area_width/2,\
        border_strip_with+field_length-goal_area_length, border_strip_with+field_width/2+goal_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-goal_area_length, border_strip_with+field_width/2-goal_area_width/2,\
        border_strip_with+field_length, border_strip_with+field_width/2-goal_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-goal_area_length, border_strip_with+field_width/2+goal_area_width/2,\
        border_strip_with+field_length, border_strip_with+field_width/2+goal_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with+field_width/2+goal_area_width/2,\
        border_strip_with+goal_area_length, border_strip_with+field_width/2+goal_area_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with, border_strip_with+field_width/2-goal_area_width/2,\
        border_strip_with+goal_area_length, border_strip_with+field_width/2-goal_area_width/2),\
        fill=line_color, width=6)

draw.ellipse((border_strip_with+field_length/2-center_circle_dia/2, border_strip_with+field_width/2-center_circle_dia/2,\
        border_strip_with+field_length/2+center_circle_dia/2,border_strip_with+field_width/2+center_circle_dia/2 ), outline=line_color, width=6)
draw.line((border_strip_with+field_length/2-10, border_strip_with+field_width/2,\
        border_strip_with+field_length/2+10, border_strip_with+field_width/2),\
        fill=line_color, width=6)

draw.line((border_strip_with+penalty_mark_dist-10, border_strip_with+field_width/2,\
        border_strip_with+penalty_mark_dist+10, border_strip_with+field_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+penalty_mark_dist, border_strip_with+field_width/2-10,\
        border_strip_with+penalty_mark_dist, border_strip_with+field_width/2+10),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-penalty_mark_dist-10, border_strip_with+field_width/2,\
        border_strip_with+field_length-penalty_mark_dist+10, border_strip_with+field_width/2),\
        fill=line_color, width=6)
draw.line((border_strip_with+field_length-penalty_mark_dist, border_strip_with+field_width/2-10,\
        border_strip_with+field_length-penalty_mark_dist, border_strip_with+field_width/2+10),\
        fill=line_color, width=6)

im.save('./hlfield_new.png', quality=95)
