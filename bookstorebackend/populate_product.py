from products.models import Products

Products.objects.create(
    id=10001,
    name="Basics To Advanced In React",
    overview="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error unde quisquam magni vel eligendi nam.",
    long_description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Soluta aut, vel ipsum maxime quam quia, quaerat tempore minus odio exercitationem illum et eos, quas ipsa aperiam magnam officiis libero expedita quo voluptas deleniti sit dolore? Praesentium tempora cumque facere consectetur quia, molestiae quam, accusamus eius corrupti laudantium aliquid! Tempore laudantium unde labore voluptates repellat, dignissimos aperiam ad ipsum laborum recusandae voluptatem non dolore. Reiciendis cum quo illum. Dolorem, molestiae corporis.",
    price=29,
    poster="https://images.unsplash.com/photo-1633356122544-f134324a6cee?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=650&q=40",
    image_local="/assets/images/10001.avif",
    rating=5,
    in_stock=True,
    size=5,
    best_seller=True,
)

Products.objects.create(
    id=10002,
    name="Django Framework for Beginners",
    overview="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error unde quisquam magni vel eligendi nam.",
    long_description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Soluta aut, vel ipsum maxime quam quia, quaerat tempore minus odio exercitationem illum et eos, quas ipsa aperiam magnam officiis libero expedita quo voluptas deleniti sit dolore? Praesentium tempora cumque facere consectetur quia, molestiae quam, accusamus eius corrupti laudantium aliquid! Tempore laudantium unde labore voluptates repellat, dignissimos aperiam ad ipsum laborum recusandae voluptatem non dolore. Reiciendis cum quo illum. Dolorem, molestiae corporis.",
    price=19,
    poster="https://images.unsplash.com/photo-1580894894513-541e068a3e2b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=650&q=40",
    image_local="/assets/images/10002.avif",
    rating=5,
    in_stock=True,
    size=2,
    best_seller=False,
)

# Add similar blocks for other products (id: 10003 to 10010)


