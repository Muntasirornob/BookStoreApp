import {Routes,Route} from "react-router-dom";

import { Home } from "../pages/home/components/Home";


export const AllRoutes = () => {

    return (
        <>
        <Routes>
            <Route path="/" element ={<Home/>}/>
            
        </Routes>
        </>

    )

}