namespace PoPClient
{
    class Program
    {
        static void Main(string[] args)
        {
            ApiProxy client = new ApiProxy("http://localhost:8600");
            App app = new App(client);

            app.RunAsync().Wait();
        }
    }
}
