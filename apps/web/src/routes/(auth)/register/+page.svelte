<script lang="ts">
	import { resolve } from '$app/paths';
</script>

<svelte:head>
  <title>Create Account | MyBrand</title>
</svelte:head>

<div class="text-center space-y-2 mb-8">
  <h1 class="text-3xl font-bold tracking-tight text-base-content">Create your account</h1>
  <p class="text-sm text-base-content/60">Join 24,000 developers to build amazing apps</p>
</div>

<div class="grid grid-cols-2 gap-4 mb-6">
  <button class="btn btn-outline border-base-300 hover:bg-base-200 text-base-content capitalize">
    <img src="https://authjs.dev/img/providers/google.svg" class="w-5 h-5 mr-2" alt="Google" />
    Google
  </button>
  <button class="btn btn-black bg-black text-white hover:bg-black/80 capitalize">
    <img src="https://authjs.dev/img/providers/github.svg" class="w-5 h-5 mr-2 invert" alt="GitHub" />
    GitHub
  </button>
</div>

<div class="divider text-xs text-base-content/40 uppercase">Or sign up with email</div>

<form method="POST" class="space-y-4">
  <div class="relative">
    <span class="absolute inset-y-0 left-3 flex items-center text-base-content/40">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" /></svg>
    </span>
    <input type="text" placeholder="Full Name" class="input input-bordered w-full pl-10 focus:input-primary" />
  </div>

  <div class="relative">
    <span class="absolute inset-y-0 left-3 flex items-center text-base-content/40">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" /></svg>
    </span>
    <input type="email" placeholder="you@example.com" class="input input-bordered w-full pl-10 focus:input-primary" />
  </div>

  <div class="relative">
    <span class="absolute inset-y-0 left-3 flex items-center text-base-content/40">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0V10.5m-2.812 9H20.25m-15.75 0V12a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v7.5m-15.75 0h15.75" /></svg>
    </span>
    <input type="password" placeholder="Password" class="input input-bordered w-full pl-10 pr-10 focus:input-primary" />
    <button type="button" class="absolute inset-y-0 right-3 flex items-center text-base-content/40 hover:text-primary">
       <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" /></svg>
    </button>
  </div>

  <div class="form-control">
    <label class="label cursor-pointer justify-start gap-3">
      <input type="checkbox" class="checkbox checkbox-sm checkbox-primary rounded-full" />
      <span class="label-text text-base-content/70">I agree to the <a href={resolve("/terms")} class="text-primary hover:underline underline-offset-4">Terms & Conditions</a></span>
    </label>
  </div>

  <button class="btn btn-neutral w-full bg-base-100 hover:bg-base-200 text-base-content border-base-300 mt-2">Sign up</button>
</form>

<p class="text-center text-sm text-base-content/60 mt-6">
  Already have an account? <a href={resolve("/login")} class="text-primary font-medium hover:underline">Sign in</a>
</p>