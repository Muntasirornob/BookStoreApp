import React from 'react'
import {Hero} from "./components/Hero"
import {FeaturedProducts} from "./components/FeatureProduct"
import {Testimonial} from "./components/Testomonial"
import {Faq}  from "./components/Faq"

export const Home = () => {
  return (
    <div>
        
        <Hero/>
        <FeaturedProducts />
        <Testimonial/>
        <Faq />
      
    </div>
  )
}
