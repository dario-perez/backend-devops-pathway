interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  stock: number;
}

const inventory: Product[] = [
  { id: 101, name: "Mouse Gamer", price: 25, category: "Accesorios", stock: 10 },
  { id: 102, name: "Teclado Mecánico", price: 80, category: "Accesorios", stock: 0 },
  { id: 103, name: "Monitor 4K", price: 400, category: "Monitores", stock: 5 },
  { id: 104, name: "Cable HDMI", price: 10, category: "Accesorios", stock: 20 },
]

function productFilter(category: string) {
  const filteredProducts = inventory.filter(c => c.category === category && c.stock > 0)
  return filteredProducts.map(p => {
    const onSale = p.price * 0.9;

    if (category.toLowerCase() === 'accesorios') {
      return `10% OFF: ${p.name} - $${onSale}`;
    }

    return `${p.name} - ${p.price}`
  })
}