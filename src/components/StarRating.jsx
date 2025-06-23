import React from 'react'
import { FaStar } from 'react-icons/fa'




function StarRating({ value, onChange }) {
  return (
    <div className='flex'>
        {[...Array(5)].map((_, index) => {
            const ratingValue = index + 1
            return (
                <label key={index}>
                    <input 
                        type="radio"
                        name="rating"
                        value={ratingValue}
                        className='hidden'
                        onClick={() => onChange(ratingValue)}
                    />
                    <FaStar className={`cursor-pointer text-2xl ${ratingValue <= value ? 'text-yellow-400' : 'text-gray-300'}`} />
                </label>
            )
        }
    )}
    </div>
  )
}

export default StarRating