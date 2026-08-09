<script>
  // Mock data for activities
  let activities = $state([
    { id: 1, user: 'Alice', action: 'Created Project: "Alpha"', type: 'create', time: '2 mins ago', icon: '🚀' },
    { id: 2, user: 'Bob', action: 'Updated Billing Info', type: 'billing', time: '1 hour ago', icon: '💳' },
    { id: 3, user: 'Charlie', action: 'Joined the Team', type: 'user', time: '3 hours ago', icon: '👤' },
    { id: 4, user: 'System', action: 'Backup Completed', type: 'system', time: '5 hours ago', icon: '💾' },
    { id: 5, user: 'Alice', action: 'Deleted Draft: "Test"', type: 'delete', time: 'Yesterday', icon: '🗑️' }
  ]);

  let filter = $state('all');

  // Filter logic (Svelte 5 Derived State)
  let filteredActivities = $derived(
    filter === 'all' ? activities : activities.filter(a => a.type === filter)
  );
</script>

<div class="max-w-5xl mx-auto space-y-6">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-base-100 p-4 rounded-xl shadow-sm border border-base-200">
    <div>
      <h1 class="text-2xl font-bold">Activity Logs</h1>
      <p class="text-sm text-base-content/60">Tracking all actions across your organization.</p>
    </div>
    
    <div class="join">
      <button class="btn btn-sm join-item {filter === 'all' ? 'btn-active' : ''}" onclick={() => filter = 'all'}>All</button>
      <button class="btn btn-sm join-item {filter === 'create' ? 'btn-active' : ''}" onclick={() => filter = 'create'}>Creates</button>
      <button class="btn btn-sm join-item {filter === 'system' ? 'btn-active' : ''}" onclick={() => filter = 'system'}>System</button>
    </div>
  </div>

  <div class="card bg-base-100 shadow-xl border border-base-200">
    <div class="card-body">
      <ul class="timeline timeline-vertical timeline-compact">
        {#each filteredActivities as item, i (item.id)}
          <li>
            {#if i !== 0}<hr />{/if}
            <div class="timeline-middle">
              <div class="w-8 h-8 rounded-full bg-base-200 flex items-center justify-center text-lg">
                {item.icon}
              </div>
            </div>
            <div class="timeline-end mb-10 ml-4">
              <time class="font-mono italic text-xs opacity-50">{item.time}</time>
              <div class="text-lg font-black">{item.user}</div>
              <p class="text-base-content/70">{item.action}</p>
              
              {#if item.type === 'create'}
                <button class="btn btn-xs btn-outline btn-primary mt-2">View Details</button>
              {/if}
            </div>
            {#if i !== filteredActivities.length - 1}<hr />{/if}
          </li>
        {/each}
      </ul>

      {#if filteredActivities.length === 0}
        <div class="text-center py-10">
          <p class="text-base-content/40 italic">No activities found for this filter.</p>
        </div>
      {/if}
    </div>
  </div>

  <div class="flex justify-center mt-6">
    <div class="join">
      <button class="join-item btn btn-sm">«</button>
      <button class="join-item btn btn-sm">Page 1</button>
      <button class="join-item btn btn-sm">»</button>
    </div>
  </div>
</div>