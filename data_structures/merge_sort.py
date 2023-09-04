from linked_list import LinkedList

def merge_sort(collection):
    if isinstance(collection, LinkedList):
        if collection.size() <= 1:
            return collection
        
        def split(group):
            mid_point = group.size() // 2 - 1
            mid = group.get(mid_point)
            right = LinkedList()
            right.head = mid.next
            mid.next = None
            return group, right
        
        left_side, right_side = split(collection)

        left = merge_sort(left_side)
        right = merge_sort(right_side)

        def merge(l, r):
            merged = LinkedList()
            while l.head or r.head:
                if r.head == None or (l.head and l.head.data < r.head.data):
                    merged.add(l.pop())
                else:
                    merged.add(r.pop())
            return merged
        
        return merge(left, right)
    
    if len(collection) <= 1:
        return collection

    def split(group):
        mid = len(group) // 2
        return group[:mid], group[mid:]
    
    left_side, right_side = split(collection)

    left = merge_sort(left_side)
    right = merge_sort(right_side)

    def merge(l, r):
        merged = []
        while len(l) > 0 and len(r) > 0:
            merged.append(l.pop(0) if l[0] < r[0] else r.pop(0))
        return merged + l + r

    return merge(left, right)

if __name__ == "__main__":
    items = [2, 6, 3, 7, 12, 4, 18, 10, 15, 16, 1, 5, 13, 17, 24, 11, 20, 27, 21, 19, 8, 9, 26, 14, 25, 23, 22]

    sorted = merge_sort(items)
    print(sorted)

    ll = LinkedList()
    ll.addAll(items)
    print(ll)
    sorted_ll = merge_sort(ll)
    print(sorted_ll)