<script lang="ts">
  import { resolve } from '$app/paths';

  /** * Svelte 5 "Runes" Syntax:
   * $props() is how we receive data passed to this component.
   * 'children' is a special snippet that represents the page content 
   * (e.g., whatever is in your +page.svelte).
   */
  let { children } = $props();
  let notificationCount = $state(5);
  let isCollapsed = $state(false);

  function toggleSidebar() {
    isCollapsed = !isCollapsed;
  }
</script>

<div class="flex min-h-screen bg-base-200">
  <aside 
    class="bg-base-100 border-r border-base-200 transition-[width] duration-300 flex flex-col z-20
    {isCollapsed ? 'w-20' : 'w-64'}"
  >
    <div class="p-4 flex items-center {isCollapsed ? 'justify-center' : 'justify-between'} min-h-[64px]">
      {#if !isCollapsed}
        <span class="font-bold text-xl px-2 transition-opacity">MyApp</span>
      {/if}
      <button 
        class="btn btn-ghost btn-square btn-sm" 
        onclick={toggleSidebar}
        aria-label={isCollapsed ? "Expand sidebar" : "Collapse sidebar"}
      >
        <span class="icon-[heroicons-outline--bars-3-bottom-left] w-6 h-6"></span>
      </button>
    </div>

    <ul class="menu px-2 space-y-2 w-full">
      <li class="flex items-center {isCollapsed ? 'justify-center' : ''}">
        <span 
          class="menu-title opacity-50 text-xs uppercase tracking-widest px-4 w-full min-h-[1.25rem] flex items-center"
        >
          {#if !isCollapsed}
            Dashboard
          {/if}
        </span>
      </li>
      <li>
        <a 
          href={resolve("/overview")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Overview">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--chart-bar] w-6 h-6"></span>
          </div>
          {#if !isCollapsed} 
            <span class="whitespace-nowrap font-medium">Overview</span> 
          {/if}
        </a>
      </li>
      <li>
        <a 
          href={resolve("/settings")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Settings">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--cog-6-tooth] w-6 h-6"></span>
          </div>
          {#if !isCollapsed} 
            <span class="whitespace-nowrap font-medium">Settings</span> 
          {/if}
        </a>
      </li>
      <li>
        <a 
          href={resolve("/profile")} 
          class="flex items-center rounded-lg transition-all active:bg-primary/10
          {isCollapsed ? 'justify-center p-3' : 'gap-4 p-3'}"
          class:tooltip={isCollapsed}
          class:tooltip-right={isCollapsed}
          data-tip="Profile">
          <div class="flex items-center justify-center shrink-0">
            <span class="icon-[heroicons-outline--user] w-6 h-6"></span>
          </div>
          {#if !isCollapsed}
            <span class="whitespace-nowrap font-medium">Profile</span> 
          {/if}
        </a>
      </li>
    </ul>
  </aside>

  <div class="flex-1 flex flex-col min-w-0">
    <header class="navbar bg-base-100 border-b border-base-200 px-4">
      <div class="flex-1">
        {#if isCollapsed}
          <span class="font-bold text-xl tracking-tight mr-2 transition-opacity hidden md:block">MyApp</span>
        {/if}
      </div>
      <div class="flex-none w-full max-w-md">
        <div class="relative w-full">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <span class="icon-[heroicons-outline--magnifying-glass] w-5 h-5 opacity-40"></span>
          </div>
          <input 
            type="text" 
            placeholder="Search..." 
            class="input input-bordered w-full pl-10 h-10 focus:input-primary transition-[width] bg-base-200/50 border-none"
          />
        </div>
      </div>
      <div class="flex-1"></div>
      <div class="flex items-center gap-4">
        <button class="btn btn-circle btn-ghost" aria-label="{notificationCount} notifications">
          <div class="indicator">
            <span class="icon-[heroicons-outline--bell-alert] w-6 h-6"></span>
            {#if notificationCount > 0}
              <span class="badge badge-xs badge-primary indicator-item">
                {notificationCount > 9 ? '9+' : notificationCount}
              </span>
            {/if}
          </div>
        </button>
        <div class="avatar placeholder">
          <div class="bg-neutral text-neutral-content rounded-full w-8 flex items-center justify-center">
            <span class="text-xs">JD</span>
          </div>
        </div>
      </div>
    </header>
    <main class="p-6 overflow-auto">
      {@render children()}
    </main>
  </div>
</div>