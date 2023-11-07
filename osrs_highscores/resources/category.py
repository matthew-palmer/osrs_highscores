from .dotnotationcreator import dotnotation

mini_game_dic = dict()
bosses_dic = dict()
skills_dic = dict()
categories = dotnotation({
    "Skill" : skills_dic,
    "Boss" : bosses_dic,
    "MiniGame" : mini_game_dic
})
