class Arrow:
    def __init__(self, canvas, x, y, scale, color, way, init):
        self.color = color
        self.canvas = canvas
        if way == "left":
            points = [-150, 0, 0, 125, 0, 50, 150, 50, 150, -50, 0, -50, 0, -125]
        else:
            points = [-150, 50, 0, 50, 0, 125, 150, 0, 0, -125, 0, -50, -150, -50]

        delete_id = canvas.create_polygon(points, fill=color, state="hidden")
        canvas.scale(delete_id, 0, 0, scale, scale)
        points = canvas.coords(delete_id)

        for pos in range(0, len(points)):
            if pos % 2 == 0:
                points[pos] = points[pos] + x
            else:
                points[pos] = points[pos] + y

        self.id = canvas.create_polygon(points, fill=color)
        canvas.delete(delete_id)
        self.set_status(init)

    def set_status(self, status):
        if not status:
            self.canvas.itemconfig(self.id, fill='')
        else:
            self.canvas.itemconfig(self.id, fill=self.color)
