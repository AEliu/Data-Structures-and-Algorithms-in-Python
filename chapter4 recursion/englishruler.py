def draw_line(tick_length, lable=''):
    line = '-' * tick_length
    if lable:
        line += ' ' + lable
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

if __name__ == '__main__':
    draw_ruler(5, 3)