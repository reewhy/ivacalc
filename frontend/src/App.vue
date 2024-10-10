<script setup>
import ImageLoad from "@/components/ImageLoad.vue";
import ImageShow from "@/components/ImageShow.vue";
</script>

<template>
  <div class="flex gap-8 w-full justify-evenly text-white">
    <image-show></image-show>
    <image-load class="w-1/2"></image-load>
  </div>
</template>
