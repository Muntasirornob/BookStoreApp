import React from 'react'
import {Hero} from "./Hero"
import {FeaturedProducts} from "./FeatureProduct"
import {Testimonial} from "./Testomonial"
import {Faq}  from "./Faq"

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
