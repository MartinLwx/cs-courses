class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.stocks = 0

    def restock(self, num):
        """Restock num items to our vending machine"""
        self.stocks += num
        return f"Current {self.product} stock: {self.stocks}"
    
    def add_funds(self, fund):
        """Add funds to balance, return funds if no stocks"""
        if self.stocks != 0:
            self.balance += fund
            return f"Current balance: ${self.balance}"
        else:
            return f"Nothing left to vend. Please restock. Here is your ${fund}."

    def vend(self):
        """Vend a product"""
        if self.stocks == 0:
            return 'Nothing left to vend. Please restock.'
        else:
            if self.balance < self.price:
                return f"You must add ${self.price - self.balance} more funds."
            else:
                change = self.balance - self.price
                self.balance = 0
                self.stocks -= 1
                if change == 0:
                    return f"Here is your {self.product}."
                else:
                    return f"Here is your {self.product} and ${change} change."



class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        age = Mint.present_year - self.year
        if age > 50:
            return self.cents + (age - 50) 
        else:
            return self.cents


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    """
    sentinel = Link(0)
    while n > 0:
        all_but_last, last = n // 10, n % 10
        # every time we insert node in the front of the linklist
        new_node = Link(n % 10, sentinel.rest)
        sentinel.rest = new_node
        n = all_but_last
    return sentinel.rest


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    # base case 1. do thing if it is empty
    if link is Link.empty:
        return 
    # base case 2. if it is an integer
    if isinstance(link, int):
        link = fn(link)

    if isinstance(link.first, int):
        link.first = fn(link.first)
    else:
        deep_map_mut(fn, link.first)
    deep_map_mut(fn, link.rest)


def two_list(vals, amounts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and amounts are the same size. Elements in vals represent the value, and the
    corresponding element in amounts represents the number of this value desired in the
    final linked list. Assume all elements in amounts are greater than 0. Assume both
    lists have at least one element.

    >>> a = [1, 3, 2]
    >>> b = [1, 1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3, Link(2)))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    idx = 0
    sentinel = Link(0)
    pos = sentinel
    while idx < len(vals):
        val, amount = vals[idx], amounts[idx]
        for _ in range(amount):
            new_node = Link(val)
            pos.rest = new_node
            pos = pos.rest
        idx += 1
    return sentinel.rest



class VirFib():
    """A Virahanka Fibonacci number.

    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    >>> start.next()
    VirFib object, value 1
    >>> start.next().next()
    VirFib object, value 1
    >>> start.next().next().next()
    VirFib object, value 2
    >>> start.next().next().next().next()
    VirFib object, value 3
    >>> start.next().next().next().next().next()
    VirFib object, value 5
    >>> start.next().next().next().next().next().next()
    VirFib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    VirFib object, value 8
    """

    def __init__(self, value=0):
        self.value = value
        self.prev = 1

    def next(self):
        new_value = self.value + self.prev
        next_fin = VirFib(new_value)
        next_fin.prev = self.value
        return next_fin

    def __repr__(self):
        return "VirFib object, value " + str(self.value)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def bst_min(t):
        """Return the min value of the tree t"""
        if t.is_leaf():
            return t.label
        sub_branch_min = min([bst_min(b) for b in t.branches])
        return min(t.label, sub_branch_min)

    def bst_max(t):
        """Return the max value of the tree t"""
        if t.is_leaf():
            return t.label
        sub_branch_max = max([bst_max(b) for b in t.branches])
        return max(t.label, sub_branch_max)

    # base case 1. a leaf node is a BST
    if t.is_leaf():
        return True
    # base case 2. each node has at most 2 children
    if len(t.branches) > 2:
        return False
    # base case 3. a node with a single child
    # it can be considered either the left or the right
    if len(t.branches) == 1:
        return (bst_max(t.branches[0]) < t.label or bst_min(t.branches[0]) > t.label) \
                and is_bst(t.branches[0])

    left_max = bst_max(t.branches[0])
    right_min = bst_min(t.branches[1])
    #print(f"max:{left_max} min: {right_min}")
    return left_max <= t.label < right_min and is_bst(t.branches[0]) and is_bst(t.branches[1])


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
