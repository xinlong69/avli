<script>
  import { resolve } from '$app/paths';

  // Mock data for the dashboard
  let stats = $state([
    { label: 'Total Revenue', value: '$45,231', desc: '↗︎ 400 (22%)', color: 'text-primary' },
    { label: 'New Users', value: '1,200', desc: '↗︎ 90 (14%)', color: 'text-secondary' },
    { label: 'System Health', value: '99.9%', desc: 'Stable', color: 'text-success' }
  ]);

  let recentActivity = [
    { id: 1, user: 'Alice', action: 'Created new project', time: '2 mins ago' },
    { id: 2, user: 'Bob', action: 'Updated billing', time: '1 hour ago' },
    { id: 3, user: 'Charlie', action: 'Joined the team', time: '3 hours ago' }
  ];
</script>

<div class="space-y-8">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
    <div>
      <h1 class="text-3xl font-bold">Dashboard Overview</h1>
      <p class="text-base-content/60">Welcome back! Here is what's happening today.</p>
    </div>
    <div class="flex gap-2">
      <button class="btn btn-outline btn-sm">Download Report</button>
      <button class="btn btn-primary btn-sm px-6">Generate AI Insights</button>
    </div>
  </div>

  <div class="stats stats-vertical lg:stats-horizontal shadow bg-base-100 w-full border border-base-200">
    {#each stats as stat (stat.label)}
      <div class="stat">
        <div class="stat-title">{stat.label}</div>
        <div class="stat-value {stat.color}">{stat.value}</div>
        <div class="stat-desc">{stat.desc}</div>
      </div>
    {/each}
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <div class="card lg:col-span-2 bg-base-100 shadow-sm border border-base-200">
      <div class="card-body">
        <h2 class="card-title justify-between">
          Traffic Growth
          <div class="badge badge-ghost font-normal">Last 30 days</div>
        </h2>
        <div class="h-64 w-full bg-base-200/50 rounded-xl mt-4 flex items-end p-4 gap-2">
           {#each Array(12) as _, i (i)}
            <div class="bg-primary/40 w-full rounded-t" style="height: {Math.random() * 80 + 20}%"></div>
           {/each}
        </div>
      </div>
    </div>

    <div class="card bg-base-100 shadow-sm border border-base-200">
      <div class="card-body">
        <h2 class="card-title mb-4">Recent Activity</h2>
        <ul class="space-y-4">
          {#each recentActivity as item (item.id)}
            <li class="flex gap-4 items-start">
              <div class="avatar placeholder">
                <div class="bg-neutral text-neutral-content rounded-full w-8 flex items-center justify-center">
                  <span>{item.user[0]}</span>
                </div>
              </div>
              <div>
                <p class="text-sm font-medium">
                  <span class="text-primary">{item.user}</span> {item.action}
                </p>
                <p class="text-xs text-base-content/50">{item.time}</p>
              </div>
            </li>
          {/each}
        </ul>
        <div class="card-actions mt-6">
          <a href={resolve('/overview/activity')} class="btn btn-ghost btn-block btn-sm">View All History</a>
        </div>
      </div>
    </div>
  </div>
</div>