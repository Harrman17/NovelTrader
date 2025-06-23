import React from "react"


function Landing() {
  return (
    <div className="bg-gray-50 min-h-screen">
        <div className="p-7 flex flex-col gap-4">
            <h1 className="font-bold text-3xl">Tell us <span className="text-accent">what matters most</span> - and we'll do the rest</h1>
            <h2 className="font-medium text-xl">We match you with the best car options based on what you care about</h2>
            <p>🧠 We match you with the best car options based on what you care about</p>
            <p>🚗 You get matched with cars tailored to your lifestyle</p>
            <button className="bg-accent text-white rounded-lg w-40 p-2 mt-2 ">Find your next car</button>
        </div>
        <div>
            <img src="/blueCars.png" />
        </div>
    </div>
  )
 }

export default Landing;
