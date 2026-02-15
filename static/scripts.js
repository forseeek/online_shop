function updateRatingStars(ratingDiv) {
  // get rating from rating div
  const rating = parseFloat(ratingDiv.getAttribute('data-rating')) || 0
  // get stars div block
  const stars = ratingDiv.querySelectorAll('.star')

  // run code for every star in stars div
  stars.forEach((star, index) => {
    // set star number
    const starNumber = index + 1

    // for example:  rating 3.2  starNumber 3
    // 3.2 >= 3 -> true, then add "full" class for star #3
    if (rating >= starNumber) {
      star.classList.add('full')
      star.style.background = 'none'
    }
    // for example:  rating 3.2  starNumber 4
    // 3.2 > 4 - 1 -> true, then fill only 20% of star #4 with color
    else if (rating > starNumber - 1) {
      const fillPercent = (rating - (starNumber - 1)) * 100
      star.style.background = `linear-gradient(90deg, #38ddca ${fillPercent}%, #bbbdbc ${fillPercent}%)`
      star.style.webkitBackgroundClip = 'text'
      star.style.webkitTextFillColor = 'transparent'
      star.style.backgroundClip = 'text'
    }
    // for example:  rating 3.2  starNumber 5
    // 3.2 >= 5     -> false
    // 3.2 >  5 - 1 -> false
    // then remove "full" class for star #4
    else {
      star.classList.remove('full')
      star.style.background = 'none'
    }
  })
}

// when page loads run updateRatingStars function
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.rating').forEach(updateRatingStars)
})
