<script setup>
import ImageLoad from "@/components/ImageLoad.vue";
import ImageShow from "@/components/ImageShow.vue";
</script>

<template>
  <div class="flex gap-8 w-full justify-evenly text-white">
    <image-show class="max-w-[70%]"></image-show>
    <image-load></image-load>
  </div>
</template>
