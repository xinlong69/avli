<script lang="ts">
  import { resolve } from '$app/paths';
  
  const registerPath = resolve('/register');
</script>

<svelte:head>
  <title>Login | MyBrand</title>
</svelte:head>

<div class="text-center space-y-2 mb-8">
  <h1 class="text-4xl font-extrabold tracking-tight text-white drop-shadow-sm">
    Ready for take-off?
  </h1>
  <p class="text-base text-white/80 font-medium">
    Log in to start planning your next adventure.
  </p>
</div>

<div class="grid grid-cols-2 gap-4 mb-6">
  <button class="btn btn-outline border-base-300 hover:bg-base-200 text-base-content capitalize font-medium bg-white/50">
    <img src="https://authjs.dev/img/providers/google.svg" class="w-5 h-5 mr-2" alt="Google" />
    Google
  </button>
  <button class="btn btn-black bg-black text-white hover:bg-black/80 border-none capitalize font-medium">
    <img src="https://authjs.dev/img/providers/github.svg" class="w-5 h-5 mr-2 invert" alt="GitHub" />
    GitHub
  </button>
</div>

<div class="divider text-xs text-base-content/40 uppercase font-semibold">or sign in with email</div>

<form method="POST" class="space-y-4">
  <div class="relative">
    <span class="absolute inset-y-0 left-3 flex items-center text-base-content/40">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" /></svg>
    </span>
    <input type="email" name="email" placeholder="Email address" class="input input-bordered w-full pl-10 focus:input-primary bg-white/50" required />
  </div>

  <div class="relative">
    <span class="absolute inset-y-0 left-3 flex items-center text-base-content/40">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0V10.5m-2.812 9H20.25m-15.75 0V12a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v7.5m-15.75 0h15.75" /></svg>
    </span>
    <input type="password" name="password" placeholder="Password" class="input input-bordered w-full pl-10 pr-10 focus:input-primary bg-white/50" required />
  </div>

  <div class="flex items-center justify-between mt-2">
    <label class="label cursor-pointer justify-start gap-2">
      <input type="checkbox" class="checkbox checkbox-sm checkbox-primary rounded" />
      <span class="label-text text-xs text-base-content/70">Remember me</span>
    </label>
  </div>

  <button class="btn btn-neutral w-full bg-black text-white border-none hover:bg-black/90 mt-4 h-12 shadow-lg">
    Let's Go!
  </button>
</form>

<p class="text-center text-sm text-black mt-8">
  Don't have an account? <a href={registerPath} class="text-blue-700 font-bold hover:underline">Join for free</a>
</p>