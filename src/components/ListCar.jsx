import React, { useState } from "react";

function ListCar() {
  const [showMOT, setShowMOT] = useState(false);

  return (
    <div className="p-6 max-w-3xl mx-auto bg-white rounded-md">
      <h1 className="text-2xl font-bold text-center mb-4">Get your car listed!</h1>

      <div className="flex gap-2 mb-6">
        <input
          type="text"
          placeholder="Enter your number plate"
          className="flex-1 border border-gray-300 p-2 rounded"
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded">Look up</button>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div>
          <label className="block">Make</label>
          <input type="text" className="border p-2 rounded w-full" />
        </div>
        <div>
          <label className="block">Model</label>
          <input type="text" className="border p-2 rounded w-full" />
        </div>

        <div>
          <label className="block">Year of Manufacture</label>
          <select className="border p-2 rounded w-full">
            <option> </option>
            <option>2000</option>
            <option>2001</option>
            <option>2002</option>
            <option>2003</option>
            <option>2004</option>
            <option>2005</option>
            <option>2006</option>
            <option>2007</option>
            <option>2008</option>
            <option>2009</option>
            <option>2010</option>
            <option>2011</option>
            <option>2012</option>
            <option>2013</option>
            <option>2014</option>
            <option>2015</option>
            <option>2016</option>
            <option>2017</option>
            <option>2018</option>
            <option>2019</option>
            <option>2020</option>
            <option>2021</option>
            <option>2022</option>
            <option>2023</option>
            <option>2024</option>
            <option>2025</option>
          </select>
        </div>

        <div>
        <label className="block">Colour</label>
          <select className="border p-2 rounded w-full">
            <option> </option>
            <option>Blue</option>
            <option>Black</option>
            <option>Silver</option>
            <option>Grey</option>
            <option>White</option>
            <option>Red</option>
            <option>Green</option>
            <option>Orange</option>
            <option>Beige</option>
            <option>Brown</option>
            <option>Other</option>
          </select>
        </div>
        
      

        <div>
          <label>Engine Size</label>
          <select className="border p-2 rounded w-full">
            <option> </option>
            <option>1.0L</option>
            <option>1.2L</option>
            <option>1.4L</option>
            <option>1.6L</option>
            <option>1.8L</option>
            <option>2.0L</option>
            <option>2.2L</option>
            <option>3.0L</option>
            <option>4.0L</option>
          </select>
        </div>

        <div>
          <label>Mileage</label>
          <input className="border p-2 rounded w-full" type="number"/>
        </div>

        <div>
          <label>Transmission</label>
          <select className="border p-2 rounded w-full">
            <option> </option>
            <option>Manual</option>
            <option>Automatic</option>
          </select>
        </div>

        <div>
          <label>Fuel Type</label>
          <select className="border p-2 rounded w-full">
            <option> </option>
            <option>Petrol</option>
            <option>Diesel</option>
            <option>Electric</option>
          </select>
        </div>
      </div>

      <div className="mb-4">
        <label className="font-medium">Service history</label>
        <select className="border p-2 rounded w-full">
          <option> </option>
          <option>Full Service History</option>
          <option>Partial Service History</option>
          <option>Digital Service History</option>
          <option>Self Service History</option>
          <option>No Service History</option>
          <option>Don't Know</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="font-medium">Previous owners</label>
        <select className="w-full border p-2 rounded mt-1">
          <option> </option>
          <option>N/A</option>
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3+</option>
        </select>
      </div>

      {/* MOT toggle */}
      <div className="mb-6">
        <button
          onClick={() => setShowMOT(!showMOT)}
          className="text-blue-600 underline"
        >
          MOT History
        </button>
        {showMOT && (
          <div className="mt-2 p-3 border rounded bg-gray-50 text-sm">
            {/* Replace with actual MOT info or fetch dynamically */}
            <p>✅ Passed: 12 March 2024</p>
            <p>❌ Advisory: Rear brake pads close to limit</p>
            <p>✅ Passed: 18 March 2023</p>
          </div>
        )}
      </div>

      <h2 className="font-bold mb-2">Price & Sale Info</h2>
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="relative w-full">
          <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-500 text-sm">£</span>
          <input type="number" placeholder="Price" className="pl-7 pr-3 py-2 border rounded-md w-full"/>
        </div>
        <input type="text" placeholder="Location" className="border p-2 rounded" />
      </div>

      <div className="border-dashed border-2 border-gray-300 p-6 rounded text-center">
        <p className="text-gray-600 mb-2">Drag and drop or choose files</p>
        <input type="file" multiple className="mx-auto" />
      </div>
    </div>
  );
}

export default ListCar;
