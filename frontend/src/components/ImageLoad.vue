<script setup>
import axios from 'axios';
import {ref} from "vue";
let imageName = ref('')

function calcola(){
  fetch("http://127.0.0.1:5000")
      .then(res => console.log(res))
      .then(() => {
          setTimeout(()=>{

            location.reload();

          }, 1000)
        }
      )
}

function getImageUrl(){
  let name = imageName.value
  console.log(name)
  return new URL(`../../../${name}`, import.meta.url).href
}


function onFilePicked (event) {
  console.log(event.target.files[0]);
  let fileToUpload = event.target.files[0];
  let formData = new FormData();
  imageName.value = fileToUpload.name;

  formData.append("newimg", fileToUpload);

  axios.post("http://127.0.0.1:5000/success", formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(function (response) {
      console.log(response)

  })
}
</script>

<template>
  <div class="grid gap-8 max-h-1 text-xl">

    <div class="flex items-center justify-center w-full">
      <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 p-12 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
        <div class="flex flex-col items-center justify-center pt-5 pb-6">
          <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
          </svg>
          <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
          <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
        </div>
        <input id="dropzone-file"
               type="file"
               class="hidden"
               ref="file"
               accept="image/*"
               @change="onFilePicked"
        />
      </label>
    </div>
    <button class="border-2 border-gray-400 rounded-3xl p-12" @click="calcola">Calcola</button>
    <img :src="getImageUrl()">
  </div>
</template>