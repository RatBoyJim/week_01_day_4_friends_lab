def get_name(name):
   return name["name"]

def get_favourite_tv_show(show):
    return show["tv_show"]

def test_person_likes_food__True(food, person):
    if person["snacks"] == food:
        return True
    else:
        return False