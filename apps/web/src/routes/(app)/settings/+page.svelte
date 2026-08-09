<script>
  // Svelte 5 state for preferences
  let notifications = $state({
    email: true,
    desktop: false,
    marketing: false
  });
  
  let theme = $state("dark");
  let language = $state("en");

  // Effect to update the DOM whenever the theme state changes
  $effect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    // Optional: Save to localStorage so it persists on refresh
    localStorage.setItem('theme', theme);
  });

  // Optional: Load saved theme on mount
  $effect(() => {
    const saved = localStorage.getItem('theme');
    if (saved) theme = saved;
  });
</script>

<div class="max-w-4xl mx-auto space-y-6 pb-12">
  <h1 class="text-3xl font-bold">App Settings</h1>
  <div class="card bg-base-100 shadow-xl border border-base-200">
    <div class="card-body">
      <h2 class="card-title flex items-center gap-2">
        <span class="icon-[heroicons-outline--adjustments-horizontal] w-5 h-5 text-primary"></span>
        General
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-4">
        <div class="form-control w-full">
          <label class="label" for="lang-select">
            <span class="label-text font-semibold">Display Language</span>
          </label>
          <select id="lang-select" class="select select-bordered focus:select-primary" bind:value={language}>
            <option value="en">English (US)</option>
            <option value="es">Español</option>
            <option value="fr">Français</option>
          </select>
        </div>

        <div class="form-control w-full">
          <label class="label" for="theme-select">
            <span class="label-text font-semibold">System Theme</span>
          </label>
          <select id="theme-select" class="select select-bordered focus:select-primary" bind:value={theme}>
            <option value="light">Light Mode</option>
            <option value="dark">Dark Mode</option>
            <option value="cupcake">Cupcake (Pastel)</option>
            <option value="nord">Nord (Arctic)</option>
          </select>
        </div>
      </div>
    </div>
  </div>

  <div class="card bg-base-100 shadow-xl border border-base-200">
    <div class="card-body">
      <h2 class="card-title flex items-center gap-2">
        <span class="icon-[heroicons-outline--bell] w-5 h-5 text-primary"></span>
        Notifications
      </h2>
      <p class="text-sm text-base-content/60 mb-4">Manage how and when you receive updates.</p>

      <div class="space-y-2">
        <label class="label cursor-pointer hover:bg-base-200/50 rounded-lg px-2 transition-colors">
          <span class="label-text">Email updates for new activity</span>
          <input type="checkbox" class="toggle toggle-primary" bind:checked={notifications.email} />
        </label>
        
        <label class="label cursor-pointer hover:bg-base-200/50 rounded-lg px-2 transition-colors">
          <span class="label-text">Desktop push notifications</span>
          <input type="checkbox" class="toggle toggle-primary" bind:checked={notifications.desktop} />
        </label>

        <label class="label cursor-pointer hover:bg-base-200/50 rounded-lg px-2 transition-colors">
          <span class="label-text">Weekly marketing summary</span>
          <input type="checkbox" class="toggle toggle-primary" bind:checked={notifications.marketing} />
        </label>
      </div>

      <div class="card-actions justify-end mt-6">
        <button class="btn btn-primary btn-sm">Save Preferences</button>
      </div>
    </div>
  </div>
</div>