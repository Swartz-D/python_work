def sandwich_maker(*fixins):
    """Print sandwich ingredients"""
    order = f"You ordered a sandwich with: {fixins}"
    print(order)


sandwich_maker('turkey', 'tomato', 'lettuce', 'bacon', 'mayo', 'pickles')
sandwich_maker('ham', 'salami', 'swiss', 'shredded lettuce')
