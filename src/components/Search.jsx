import React from 'react'
import { useState } from 'react'
import StarRating from './StarRating'

function Search() {

  const [priorities, setPriorities] = useState({
    budget: 0,
    runningCost: 0,
    maintenance: 0,
    mileage: 0,
    depreciation: 0,
    insurance: 0,
    modability: 0,
    motHistory: 0,
  })

  const handlePriorityChange = (feature, rating) => {
    setPriorities(prev => ({ ...prev, [feature]: rating }));
  }



  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 pb-65">
      <div className="bg-gray-50 rounded-xl shadow-md p-8 w-full max-w-2xl">
        <h1 className="text-3xl font-bold text-center text-gray-900 mb-2">
          Find your next car
        </h1>
        <p className="text-center text-gray-600 mb-6">
          Search from thousands of new and used cars.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Postcode
            </label>
            <input
              type="text"
              placeholder="Enter postcode"
              className="w-full border rounded-md px-3 py-2"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Distance
            </label>
            <select className="w-full border rounded-md px-3 py-2">
              <option>National</option>
              <option>Within 5 miles</option>
              <option>Within 10 miles</option>
              <option>Within 15 miles</option>
              <option>Within 20 miles</option>
              <option>Within 25 miles</option>
              <option>Within 30 miles</option>
              <option>Within 35 miles</option>
              <option>Within 40 miles</option>
              <option>Within 45 miles</option>
              <option>Within 50 miles</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Maximum Mileage
            </label>
            <select className="w-full border rounded-md px-3 py-2">
              <option>0 miles</option>
              <option>10,000 miles</option>
              <option>20,000 miles</option>
              <option>30,000 miles</option>
              <option>40,000 miles</option>
              <option>50,000 miles</option>
              <option>60,000 miles</option>
              <option>70,000 miles</option>
              <option>80,000 miles</option>
              <option>90,000 miles</option>
              <option>100,000 miles</option>
              <option>110,000 miles</option>
              <option>120,000 miles</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Budget
            </label>
            <div className="relative">
              <span className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500">£</span>
              <input
                
                type="number"
                className="w-full pl-8 pr-3 py-2 border rounded-md"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Transmission
            </label>
            <select className="w-full border rounded-md px-3 py-2">
              <option>Any</option>
              <option>Manual</option>
              <option>Automatic</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Engine Size
            </label>
            <select className="w-full border rounded-md px-3 py-2">
              <option>Any</option>
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
        </div>

        <div>
          <h2 className=' mt-7 mb-2 text-xl'>Tell us what matters most - and we'll do the rest</h2>
          <div className="space-y-4">
            {[
              { key: 'budget', label: 'Budget' },
              { key: 'runningCost', label: 'Low running cost – fuel, road tax' },
              { key: 'maintenance', label: 'Low Maintenance Costs (reliability), repairs' },
              { key: 'mileage', label: 'Mileage' },
              { key: 'depreciation', label: 'Low Depreciation & High Resale Value' },
              { key: 'insurance', label: 'Insurance group' },
              { key: 'modability', label: 'Modability' },
              { key: 'motHistory', label: 'Good MOT history' },
            ].map(({ key, label }) => (
              <div key={key} className="flex justify-between items-center">
                <span className="text-gray-700">{label}</span>
                <StarRating value={priorities[key]} onChange={(value) => handlePriorityChange(key, value)} />
              </div>
            ))}
          </div>
        </div>



        <button className="w-full mt-6 bg-blue-600 text-white font-semibold py-3 rounded-md hover:bg-blue-700 transition">
          Search
        </button>
      </div>
    </div>

  )
}

export default Search