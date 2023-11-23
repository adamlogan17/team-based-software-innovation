
/**
 * Fetches a set of random dog images from the Dog CEO's Dog API and displays them on the web page.
 * The images are loaded into the 'imageContainer' element.
 * @Author - Code written by @AdamLogan, docstring by @DeanLogan
 * @async
 * @function
 * @returns {Promise<void>} A promise that resolves when the images are successfully loaded and displayed.
 */
async function displayImages() {
  $.get('https://dog.ceo/api/breeds/image/random/50', 
    function (data) {
      const images = data.message;
      const imageContainer = document.getElementById('imageContainer');
      imageContainer.innerHTML = ''; // Clear the container
      images.forEach(url => {
        const imgElement = document.createElement('img');
        imgElement.src = url;
        imgElement.style.margin = '5px';
        imageContainer.appendChild(imgElement);
      });
    });
}

window.onload = displayImages();