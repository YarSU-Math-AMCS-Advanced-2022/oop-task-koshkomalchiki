from Checkers import Checkers


class OptionsMenu:
    # Выводит меню выбора действий над реакцией (поставить/убрать)
    def create(
            menu: dict[str, str],
            messege: str = ''
    ) -> str:
        # Проверки соответствия типов
        Checkers.type_comparison(
            value=menu,
            type_name=dict,
            function_name='OptionsMenu.create()'
        )
        Checkers.type_comparison(
            value=messege,
            type_name=str,
            function_name='OptionsMenu.create()'
        )

        action_is_correct = False
        while not action_is_correct:
            print('\n ' + messege)
            for symbol, option in menu.items():
                symbol = 'Enter' if symbol == '' else symbol
                print(f'  [ {symbol.strip()} ] {option}')
            action = input(' -> ').strip()

            action_is_correct = action in menu.keys()
            if not action_is_correct:
                print('Указан не существующий вариант. Повторите попытку.')

        return action
