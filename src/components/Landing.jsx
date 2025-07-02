import React from "react"


function Landing({ onFindClick }) {
  return (
    <div className="bg-gray-50 min-h-screen flex flex-col sm:flex-row">
        <div className="p-7 flex flex-col gap-4 sm:p-7 sm:mt-10">
            <h1 className="font-bold text-3xl sm:text-5xl">Tell us <span className="text-accent relative after:absolute after:left-0 after:bottom-0 after:h-[2px] after:w-full after:bg-accent after:scale-x-0 hover:after:scale-x-100 after:origin-left after:transition-transform after:duration-300">what matters most</span><br /> - and we'll do the rest</h1>
            <h2 className="font-medium text-xl sm:text-2xl">We match you with the best car options based on what you care about</h2>
            <p className="sm:text-lg">🧠 We crunch the information using listings & vehicle data</p>
            <p className="sm:text-lg">🚗 You get matched with cars tailored to your lifestyle</p>
            <button className="bg-accent text-white rounded-lg w-40 p-2 mt-2 sm:text-lg sm:w-50" onClick={onFindClick}>Find your next car</button>
        </div>
        <div className="flex justify-end mt-12 sm:h-120 sm:mt-50">
            <img src="/blueCars.png" />
        </div>
    </div>
  )
 }

export default Landing;

