import {Routes,Route} from "react-router-dom";

import { Home } from "../pages/home/Home";

import { ProductList } from "../pages/products/ProductList";


export const AllRoutes = () => {

    return (
        <>
        <Routes>
            <Route path="/" element ={<Home/>}/>
            <Route path="/products" element={<ProductList />} />
            
        </Routes>
        </>

    )

}