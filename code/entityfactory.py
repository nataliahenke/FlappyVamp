from code.background import Background


class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'lvl1bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'lvl1bg{i}', position(0, 0)))
                return list_bg
