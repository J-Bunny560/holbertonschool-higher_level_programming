from typing import SupportsIndex


class VerboseList(list):

    def append(self, item):
        """
    Appends an item to the list and prints a message.

    Args:
        item: The item to be appended to the list.
    """
        super().append(item)

        print(f"Added [{item}] to the list.")

    def extend(self, items=[]):
        """
    Extends the list with the items from an iterable and prints a message.

    Args:
        items (iterable, optional): An iterable of items to extend the list with. Defaults to an empty list.
    """
        print(f"Extended the list with [{len(items)}] items.")

        super().extend(items)

    def remove(self, item):
        """
    Removes the first occurrence of an item from the list and prints a message.

    Args:
        item: The item to be removed from the list.

    Raises:
        ValueError: If the item is not found in the list.
    """
        super().remove(item)

        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
    Removes and returns the item at the given index from the list, and prints a message.

    Args:
        index (int, optional): The index of the item to be removed and returned. Defaults to -1, which removes and returns the last item.

    Returns:
        The item that was removed.

    Raises:
        IndexError: If the list is empty or index is out of range.
    """
        item = super().pop(index)

        print(f"Popped [{item}] from the list.")
        return item
