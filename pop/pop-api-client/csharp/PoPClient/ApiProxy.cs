using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

namespace PoPClient
{
    public class ApiProxy
    {
        private readonly HttpClient client;

        public ApiProxy(string baseUrl)
        {
            this.client = new HttpClient();
            client.BaseAddress = new Uri(baseUrl);
        }

        /// <summary>
        /// Sets the bitcoin.fee.perkb configuration property on the miner
        /// to the value supplied as the amount parameter
        /// 
        /// e.g. PUT /api/config
        /// {
        ///     "key": "bitcoin.fee.perkb",
        ///     "value": "14000"
        /// }
        /// </summary>
        /// <param name="amount"></param>
        /// <returns></returns>
        public async Task SetTransactionFeePerKbAsync(long amount)
        {
            /* Request Object:
            
            */
            JObject body = new JObject();
            body["key"] = "bitcoin.fee.perkb";
            body["value"] = amount.ToString();

            HttpResponseMessage response = await client.PutAsync("/api/config", new StringContent(body.ToString(), Encoding.UTF8, "application/json"));
            response.EnsureSuccessStatusCode();
        }

        /// <summary>
        /// Sets the auto.mine.round{roundNumber} configuration property on the miner
        /// to the value supplied as the amount parameter
        /// 
        /// e.g. PUT /api/config
        /// {
        ///     "key": "auto.mine.round4",
        ///     "value": true
        /// }
        /// </summary>
        /// <param name="roundNumber"></param>
        /// <param name="on"></param>
        /// <returns></returns>
        public async Task SetAutoMine(int roundNumber, bool on)
        {
            JObject body = new JObject();
            body["key"] = "auto.mine.round" + roundNumber.ToString();
            body["value"] = on.ToString();

            HttpResponseMessage response = await client.PutAsync("/api/config", new StringContent(body.ToString(), Encoding.UTF8, "application/json"));
            response.EnsureSuccessStatusCode();
        }

        /// <summary>
        /// Calls the list operations endpoint of the API and counts how many of the
        /// returned operations match the action waiting for transaction
        /// 
        /// GET /api/operations
        /// 
        /// </summary>
        /// <returns></returns>
        public async Task<int> GetPendingTransactionCount()
        {
            HttpResponseMessage response = await client.GetAsync("/api/operations");
            String body = await response.Content.ReadAsStringAsync();

            JArray obj = JArray.Parse(body);
            dynamic operations = obj;

            int count = 0;
            foreach (dynamic operation in operations)
            {
                if ("Waiting for transaction to be included in Bitcoin block".Equals(operation.action, StringComparison.OrdinalIgnoreCase))
                {
                    count++;
                }
            }

            return count;
        }

        /// <summary>
        /// Calls the mine endpoint of the API to begin a new mining operations
        /// 
        /// POST /api/mine
        /// {}
        /// 
        /// </summary>
        /// <returns></returns>
        public async Task Mine()
        {
            HttpResponseMessage response = await client.PostAsync("/api/mine", new StringContent("{}", Encoding.UTF8, "application/json"));
            response.EnsureSuccessStatusCode();

            String body = await response.Content.ReadAsStringAsync();

            JObject json = JObject.Parse(body);

            Console.WriteLine(json.ToString());
        }
    }
}
