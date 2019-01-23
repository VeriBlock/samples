using System;
using System.Threading;
using System.Threading.Tasks;

namespace PoPClient
{
    public class App
    {
        // A timer will run every 10 minutes
        private const int INTERVAL = 1000 * 60 * 10;

        private readonly ApiProxy client;
        private Timer timer;

        public App(ApiProxy apiClient)
        {
            this.client = apiClient;
        }

        public async Task RunAsync()
        {
            // Configure the miner the way we want it to begin
            try
            {
                // Set the transaction fee we want to use
                await client.SetTransactionFeePerKbAsync(14000);

                // Turn OFF auto-mine on round 1 blocks
                await client.SetAutoMine(1, false);
                
                // Turn ON auto-mine on round 2 blocks
                await client.SetAutoMine(2, true);

                // Turn OFF auto-mine on round 3 blocks
                await client.SetAutoMine(3, false);

                // Turn ON auto-mine on round 4 blocks
                await client.SetAutoMine(4, true);
            }
            catch (AggregateException e)
            {
                foreach (var inner in e.InnerExceptions)
                {
                    Console.WriteLine("ERROR: " + inner.Message);
                }
                Console.WriteLine("Error communicating with PoP Miner, exiting...");
                return;
            }

            AppState state = new AppState();
            state.Paused = false;

            // Start up the timer
            timer = new Timer(OnTimer, state, INTERVAL, INTERVAL);

            // Await for input to exit the application
            Console.WriteLine("Press ENTER to exit");
            Console.ReadLine();
        }

        private async void OnTimer(object state)
        {
            try
            {
                AppState appState = (AppState)state;

                // Check if a previous execution has already "paused"
                if (appState.Paused == true)
                {
                    // Get the count of mining operations in which the transaction is waiting to appear in a BTC block
                    int count = await client.GetPendingTransactionCount();

                    // If the count is less than five, we feel like it's "safe" to keep mining
                    if (count < 5)
                    {
                        // Turn ON auto-mine on round 2 blocks
                        await client.SetAutoMine(2, true);

                        // Turn ON auto-mine on round 4 blocks
                        await client.SetAutoMine(4, true);
                        appState.Paused = false;
                    }
                    else if (count > 10)
                    {
                        // The application is paused already and now there's 10 pending transactions,
                        // so lets also shut down auto-mining round 4 blocks
                        await client.SetAutoMine(4, false);
                    }
                }
                else
                {
                    // Get the count of mining operations in which the transaction is waiting to appear in a BTC block
                    int count = await client.GetPendingTransactionCount();
                    if (count >= 5)
                    {
                        // We're maybe a little concerned that there's five or more unconfirmed transactions,
                        // so we're going to turn off round 2 auto-mining to not keep piling on
                        await client.SetAutoMine(2, false);
                        appState.Paused = true;

                        // We're also going to submit a single transaction at 3x usual fee 
                        // to try to push the parent transactions through
                        await client.SetTransactionFeePerKbAsync(42000);
                        await client.Mine();

                        // Don't want to keep the fee high, so let's set it back to where it was originally
                        await client.SetTransactionFeePerKbAsync(14000);
                    }
                }

                state = appState;
            }
            catch (AggregateException e)
            {
                foreach (var inner in e.InnerExceptions)
                {
                    Console.WriteLine("ERROR: " + inner.Message);
                }
            }
        }
    }
}
