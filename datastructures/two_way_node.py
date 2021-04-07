from datastructures.node import Node


class TwoWayNode(Node):
    def __init__(self, **values):
        super().__init__(**values)
        self.prev = self.prev = values.get('prev')

    def __str__(self) -> str:
        # print(self.value)
        return {
            'value': self.value,
            'next': self.next,
            'prev': self.prev.__str__()
        }.__str__()
