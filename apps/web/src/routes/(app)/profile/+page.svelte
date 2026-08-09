<script>
  // In a real app, you'd fetch this from a database
  let user = $state({
    name: "Jane Doe",
    email: "jane@example.com",
    bio: "Full-stack developer loving Svelte 5 and daisyUI.",
    avatar: "JD"
  });

  let currentPassword = $state("");
  let newPassword = $state("");
  let confirmPassword = $state("");

  // Svelte 5 derived state to check if the form is valid
  let canSubmit = $derived(
    currentPassword.length > 0 && 
    newPassword.length >= 8 && 
    newPassword === confirmPassword
  );
</script>

<div class="max-w-4xl mx-auto space-y-6 pb-12">
  <h1 class="text-3xl font-bold">Profile</h1>
  <div class="card bg-base-100 shadow-xl border border-base-200">
    <div class="card-body">
      <div class="flex flex-col md:flex-row items-center gap-6">
        <div class="avatar placeholder">
          <div class="bg-primary text-primary-content rounded-full w-24 flex items-center justify-center">
            <span class="text-3xl font-bold">{user.avatar}</span>
          </div>
        </div>
        
        <div class="flex-1 text-center md:text-left">
          <h2 class="card-title text-2xl">{user.name}</h2>
          <p class="text-base-content/70">{user.email}</p>
          <div class="mt-2 flex justify-center md:justify-start gap-2">
            <span class="badge badge-outline">Pro Plan</span>
            <span class="badge badge-outline">Developer</span>
          </div>
        </div>
        <button class="btn btn-outline btn-sm">
          <span class="icon-[heroicons-outline--camera] w-4 h-4"></span>
          Change Photo
        </button>
      </div>

      <div class="divider">About Me</div>
      <p class="text-base-content/80">{user.bio}</p>

      <div class="card-actions justify-end mt-4">
        <button class="btn btn-primary btn-sm">Edit Bio</button>
      </div>
    </div>
  </div>

  <div class="card bg-base-100 shadow-xl border border-base-200">
    <div class="card-body">
      <h2 class="card-title flex items-center gap-2">
        <span class="icon-[heroicons-outline--lock-closed] w-5 h-5 text-primary"></span>
        Security & Password
      </h2>
      <p class="text-sm text-base-content/60">
        Changing your password will log you out of other devices.
      </p>
      
      <div class="divider my-2"></div>

      <div class="space-y-4 mt-2">
        <div class="form-control w-full">
          <label class="label" for="current-password">
            <span class="label-text font-semibold">Current Password</span>
          </label>
          <input 
            id="current-password"
            type="password" 
            placeholder="Enter current password" 
            class="input input-bordered w-full focus:input-primary bg-base-200/30" 
            bind:value={currentPassword}
          />
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="form-control w-full">
            <label class="label" for="new-password">
              <span class="label-text font-semibold">New Password</span>
            </label>
            <input 
              id="new-password"
              type="password" 
              placeholder="Min. 8 characters" 
              class="input input-bordered w-full focus:input-primary" 
              bind:value={newPassword}
            />
          </div>
          <div class="form-control w-full">
            <label class="label" for="confirm-password">
              <span class="label-text font-semibold">Confirm New Password</span>
            </label>
            <input 
              id="confirm-password"
              type="password" 
              placeholder="Repeat new password" 
              class="input input-bordered w-full focus:input-primary" 
              bind:value={confirmPassword}
            />
            {#if confirmPassword && newPassword !== confirmPassword}
              <label class="label">
                <span class="label-text-alt text-error">Passwords do not match</span>
              </label>
            {/if}
          </div>
        </div>
      </div>

      <div class="card-actions justify-end mt-8">
        <button 
          class="btn btn-primary btn-sm px-8" 
          disabled={!canSubmit}
        >
          Save New Password
        </button>
      </div>
    </div>
  </div>

  <div class="card border-2 border-error/20 bg-error/5 shadow-sm">
    <div class="card-body">
      <h2 class="card-title flex items-center gap-2 text-error">
        <span class="icon-[heroicons--exclamation-triangle] w-5 h-5 text-error"></span>
        Danger Zone
      </h2>
      <p>Once you delete your account, there is no going back. All data will be permanently wiped.</p>
      <div class="card-actions justify-end">
        <button class="btn btn-error btn-outline btn-sm">Delete Account</button>
      </div>
    </div>
  </div>
</div>