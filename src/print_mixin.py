class PrintMixin:
    """
    Класс-миксин, который будет при создании объекта печатать в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {repr(self)}")

    def __repr__(self) -> str:
        attributes = ", ".join([f"{v!r}" for v in self.__dict__.values()])
        return f"{self.__class__.__name__}({attributes})"