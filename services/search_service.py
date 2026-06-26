class SearchService:

    def __init__(

            self,

            providers

    ):

        self.providers = providers


    def search(

            self,

            keyword

    ):


        jobs = []


        for provider in self.providers:


            jobs.extend(

                provider.search(

                    keyword

                )

            )


        return jobs