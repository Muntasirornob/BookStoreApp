import { useEffect, useState } from "react";
import { ProductCard } from "../../components/ProductCart";
import { FilterBar } from "../../components/FilterBar";
import { useLocation, useNavigate } from "react-router-dom";

export const ProductList = () => {
    const [show, setShow] = useState(false);
    const [products, setProducts] = useState([]);
    const [searchQuery, setSearchQuery] = useState(""); // For the search input
    const location = useLocation();
    const navigate = useNavigate();

    const searchTerm = new URLSearchParams(location.search).get("q");

    // Fetch products whenever searchTerm changes
    useEffect(() => {
        async function fetchProducts() {
            const response = await fetch(`http://127.0.0.1:8000/products/?q=${searchTerm || ""}`);
            if (response.ok) {
                const data = await response.json();
                setProducts(data);
            } else {
                console.error("Failed to fetch products");
            }
        }
        fetchProducts();
    }, [searchTerm]);

    // Handle search input and update URL
    const handleSearch = (e) => {
        e.preventDefault();
        navigate(`/products?q=${searchQuery}`);
    };

    return (
        <main>
            <section className="my-5">
                <div className="my-5 flex justify-between">
                    <span className="text-2xl font-semibold dark:text-slate-100 mb-5">All eBooks</span>
                    <form onSubmit={handleSearch} className="flex items-center">
                        <input
                            type="text"
                            placeholder="Search..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="border p-2 rounded-l-lg dark:bg-gray-800 dark:text-white"
                        />
                        <button
                            type="submit"
                            className="bg-blue-500 text-white px-4 rounded-r-lg dark:bg-blue-700"
                        >
                            Search
                        </button>
                    </form>
                </div>

                <div className="flex flex-wrap justify-center lg:flex-row">
                    {products.map((product) => (
                        <ProductCard key={product.id} product={product} />
                    ))}
                </div>
            </section>

            {show && <FilterBar setShow={setShow} />}
        </main>
    );
};
