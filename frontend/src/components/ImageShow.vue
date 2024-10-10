<script setup>
function getImageUrl(){
  return new URL(`../../../output.jpg`, import.meta.url).href
}


</script>

<template>
  <img :src="getImageUrl()">
</template>