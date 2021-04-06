class Node:
    def __init__(self, **values):
        self.value = values.get('value')
        self.next = values.get('next')

    def __str__(self) -> str:
        return {
            'value': self.value,
            'next': self.next.__str__()
        }.__str__()