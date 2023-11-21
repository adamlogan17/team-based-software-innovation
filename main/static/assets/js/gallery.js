/**
 * Fetches images from the an endpoint (will be database, in future) and displays them in the "imageContainer" div.
 * @function displayImages
 * @author Adam Logan
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