class Node:
    def __init__(self, **values):
        self.value = values.get('value')
        self.next = values.get('next')
        self.prev = values.get('prev')

    def __str__(self) -> str:
        return {
            'value': self.value,
            'next': self.next.__str__(),
            'prev': self.prev
        }.__str__()
