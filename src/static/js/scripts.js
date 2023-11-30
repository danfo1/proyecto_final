function previewImage(event, querySelector) {
    const input = event.target;
    const $imgPreview = document.querySelector(querySelector);

    if (!input.files || !input.files.length) return;

    for (let i = 0; i < input.files.length; i++) {
        const file = input.files[i];
        const objectURL = URL.createObjectURL(file);

        const imgContainer = document.createElement('div');
        imgContainer.classList.add('image-container');

        const img = document.createElement('img');
        img.src = objectURL;
        img.style.maxWidth = "400px";
        img.style.maxHeight = "400px";
        img.style.marginBottom = "40px";

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Eliminar';
        deleteButton.classList.add('delete-button');

        deleteButton.addEventListener('click', function () {
            imgContainer.remove();
        });

        imgContainer.appendChild(img);
        imgContainer.appendChild(deleteButton);
        $imgPreview.appendChild(imgContainer);
    }
}
