points = 0

class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        global points
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return None
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return None
        else:
            points_for_this_place = 101 - place
            points += points_for_this_place
            return points_for_this_place

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        global points
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return None
        else:
            points_for_this_meters = meters * 0.5
            points += points_for_this_meters
            return points_for_this_meters

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        global points
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        if points_place is None or points_meters is None:
            print("Некорректные входные данные.")
            return None
        return points_place + points_meters


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))