# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, NextbillionSDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        map,
        mdm,
        areas,
        batch,
        browse,
        lookup,
        skynet,
        geocode,
        discover,
        fleetify,
        geofence,
        isochrone,
        directions,
        navigation,
        postalcode,
        revgeocode,
        autosuggest,
        autocomplete,
        multigeocode,
        optimization,
        restrictions,
        route_report,
        snap_to_roads,
        distance_matrix,
        restrictions_items,
    )
    from .resources.map import MapResource, AsyncMapResource
    from .resources.mdm import MdmResource, AsyncMdmResource
    from .resources.areas import AreasResource, AsyncAreasResource
    from .resources.batch import BatchResource, AsyncBatchResource
    from .resources.browse import BrowseResource, AsyncBrowseResource
    from .resources.lookup import LookupResource, AsyncLookupResource
    from .resources.geocode import GeocodeResource, AsyncGeocodeResource
    from .resources.discover import DiscoverResource, AsyncDiscoverResource
    from .resources.isochrone import IsochroneResource, AsyncIsochroneResource
    from .resources.directions import DirectionsResource, AsyncDirectionsResource
    from .resources.navigation import NavigationResource, AsyncNavigationResource
    from .resources.postalcode import PostalcodeResource, AsyncPostalcodeResource
    from .resources.revgeocode import RevgeocodeResource, AsyncRevgeocodeResource
    from .resources.autosuggest import AutosuggestResource, AsyncAutosuggestResource
    from .resources.autocomplete import AutocompleteResource, AsyncAutocompleteResource
    from .resources.restrictions import RestrictionsResource, AsyncRestrictionsResource
    from .resources.route_report import RouteReportResource, AsyncRouteReportResource
    from .resources.skynet.skynet import SkynetResource, AsyncSkynetResource
    from .resources.snap_to_roads import SnapToRoadsResource, AsyncSnapToRoadsResource
    from .resources.fleetify.fleetify import FleetifyResource, AsyncFleetifyResource
    from .resources.geofence.geofence import GeofenceResource, AsyncGeofenceResource
    from .resources.restrictions_items import RestrictionsItemsResource, AsyncRestrictionsItemsResource
    from .resources.multigeocode.multigeocode import MultigeocodeResource, AsyncMultigeocodeResource
    from .resources.optimization.optimization import OptimizationResource, AsyncOptimizationResource
    from .resources.distance_matrix.distance_matrix import DistanceMatrixResource, AsyncDistanceMatrixResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "NextbillionSDK",
    "AsyncNextbillionSDK",
    "Client",
    "AsyncClient",
]


class NextbillionSDK(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous NextbillionSDK client instance.

        This automatically infers the `api_key` argument from the `NEXTBILLION_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NEXTBILLION_SDK_API_KEY")
        if api_key is None:
            raise NextbillionSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the NEXTBILLION_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NEXTBILLION_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.nextbillion.io"

        custom_headers_env = os.environ.get("NEXTBILLION_SDK_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def fleetify(self) -> FleetifyResource:
        from .resources.fleetify import FleetifyResource

        return FleetifyResource(self)

    @cached_property
    def skynet(self) -> SkynetResource:
        from .resources.skynet import SkynetResource

        return SkynetResource(self)

    @cached_property
    def geocode(self) -> GeocodeResource:
        from .resources.geocode import GeocodeResource

        return GeocodeResource(self)

    @cached_property
    def optimization(self) -> OptimizationResource:
        from .resources.optimization import OptimizationResource

        return OptimizationResource(self)

    @cached_property
    def geofence(self) -> GeofenceResource:
        from .resources.geofence import GeofenceResource

        return GeofenceResource(self)

    @cached_property
    def discover(self) -> DiscoverResource:
        from .resources.discover import DiscoverResource

        return DiscoverResource(self)

    @cached_property
    def browse(self) -> BrowseResource:
        from .resources.browse import BrowseResource

        return BrowseResource(self)

    @cached_property
    def mdm(self) -> MdmResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import MdmResource

        return MdmResource(self)

    @cached_property
    def isochrone(self) -> IsochroneResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import IsochroneResource

        return IsochroneResource(self)

    @cached_property
    def restrictions(self) -> RestrictionsResource:
        from .resources.restrictions import RestrictionsResource

        return RestrictionsResource(self)

    @cached_property
    def restrictions_items(self) -> RestrictionsItemsResource:
        from .resources.restrictions_items import RestrictionsItemsResource

        return RestrictionsItemsResource(self)

    @cached_property
    def distance_matrix(self) -> DistanceMatrixResource:
        from .resources.distance_matrix import DistanceMatrixResource

        return DistanceMatrixResource(self)

    @cached_property
    def autocomplete(self) -> AutocompleteResource:
        from .resources.autocomplete import AutocompleteResource

        return AutocompleteResource(self)

    @cached_property
    def navigation(self) -> NavigationResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import NavigationResource

        return NavigationResource(self)

    @cached_property
    def map(self) -> MapResource:
        from .resources.map import MapResource

        return MapResource(self)

    @cached_property
    def autosuggest(self) -> AutosuggestResource:
        from .resources.autosuggest import AutosuggestResource

        return AutosuggestResource(self)

    @cached_property
    def directions(self) -> DirectionsResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import DirectionsResource

        return DirectionsResource(self)

    @cached_property
    def batch(self) -> BatchResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import BatchResource

        return BatchResource(self)

    @cached_property
    def multigeocode(self) -> MultigeocodeResource:
        from .resources.multigeocode import MultigeocodeResource

        return MultigeocodeResource(self)

    @cached_property
    def revgeocode(self) -> RevgeocodeResource:
        from .resources.revgeocode import RevgeocodeResource

        return RevgeocodeResource(self)

    @cached_property
    def route_report(self) -> RouteReportResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import RouteReportResource

        return RouteReportResource(self)

    @cached_property
    def snap_to_roads(self) -> SnapToRoadsResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import SnapToRoadsResource

        return SnapToRoadsResource(self)

    @cached_property
    def postalcode(self) -> PostalcodeResource:
        from .resources.postalcode import PostalcodeResource

        return PostalcodeResource(self)

    @cached_property
    def lookup(self) -> LookupResource:
        from .resources.lookup import LookupResource

        return LookupResource(self)

    @cached_property
    def areas(self) -> AreasResource:
        from .resources.areas import AreasResource

        return AreasResource(self)

    @cached_property
    def with_raw_response(self) -> NextbillionSDKWithRawResponse:
        return NextbillionSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NextbillionSDKWithStreamedResponse:
        return NextbillionSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key,
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncNextbillionSDK(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncNextbillionSDK client instance.

        This automatically infers the `api_key` argument from the `NEXTBILLION_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("NEXTBILLION_SDK_API_KEY")
        if api_key is None:
            raise NextbillionSDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the NEXTBILLION_SDK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NEXTBILLION_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.nextbillion.io"

        custom_headers_env = os.environ.get("NEXTBILLION_SDK_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def fleetify(self) -> AsyncFleetifyResource:
        from .resources.fleetify import AsyncFleetifyResource

        return AsyncFleetifyResource(self)

    @cached_property
    def skynet(self) -> AsyncSkynetResource:
        from .resources.skynet import AsyncSkynetResource

        return AsyncSkynetResource(self)

    @cached_property
    def geocode(self) -> AsyncGeocodeResource:
        from .resources.geocode import AsyncGeocodeResource

        return AsyncGeocodeResource(self)

    @cached_property
    def optimization(self) -> AsyncOptimizationResource:
        from .resources.optimization import AsyncOptimizationResource

        return AsyncOptimizationResource(self)

    @cached_property
    def geofence(self) -> AsyncGeofenceResource:
        from .resources.geofence import AsyncGeofenceResource

        return AsyncGeofenceResource(self)

    @cached_property
    def discover(self) -> AsyncDiscoverResource:
        from .resources.discover import AsyncDiscoverResource

        return AsyncDiscoverResource(self)

    @cached_property
    def browse(self) -> AsyncBrowseResource:
        from .resources.browse import AsyncBrowseResource

        return AsyncBrowseResource(self)

    @cached_property
    def mdm(self) -> AsyncMdmResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import AsyncMdmResource

        return AsyncMdmResource(self)

    @cached_property
    def isochrone(self) -> AsyncIsochroneResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import AsyncIsochroneResource

        return AsyncIsochroneResource(self)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResource:
        from .resources.restrictions import AsyncRestrictionsResource

        return AsyncRestrictionsResource(self)

    @cached_property
    def restrictions_items(self) -> AsyncRestrictionsItemsResource:
        from .resources.restrictions_items import AsyncRestrictionsItemsResource

        return AsyncRestrictionsItemsResource(self)

    @cached_property
    def distance_matrix(self) -> AsyncDistanceMatrixResource:
        from .resources.distance_matrix import AsyncDistanceMatrixResource

        return AsyncDistanceMatrixResource(self)

    @cached_property
    def autocomplete(self) -> AsyncAutocompleteResource:
        from .resources.autocomplete import AsyncAutocompleteResource

        return AsyncAutocompleteResource(self)

    @cached_property
    def navigation(self) -> AsyncNavigationResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import AsyncNavigationResource

        return AsyncNavigationResource(self)

    @cached_property
    def map(self) -> AsyncMapResource:
        from .resources.map import AsyncMapResource

        return AsyncMapResource(self)

    @cached_property
    def autosuggest(self) -> AsyncAutosuggestResource:
        from .resources.autosuggest import AsyncAutosuggestResource

        return AsyncAutosuggestResource(self)

    @cached_property
    def directions(self) -> AsyncDirectionsResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import AsyncDirectionsResource

        return AsyncDirectionsResource(self)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import AsyncBatchResource

        return AsyncBatchResource(self)

    @cached_property
    def multigeocode(self) -> AsyncMultigeocodeResource:
        from .resources.multigeocode import AsyncMultigeocodeResource

        return AsyncMultigeocodeResource(self)

    @cached_property
    def revgeocode(self) -> AsyncRevgeocodeResource:
        from .resources.revgeocode import AsyncRevgeocodeResource

        return AsyncRevgeocodeResource(self)

    @cached_property
    def route_report(self) -> AsyncRouteReportResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import AsyncRouteReportResource

        return AsyncRouteReportResource(self)

    @cached_property
    def snap_to_roads(self) -> AsyncSnapToRoadsResource:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import AsyncSnapToRoadsResource

        return AsyncSnapToRoadsResource(self)

    @cached_property
    def postalcode(self) -> AsyncPostalcodeResource:
        from .resources.postalcode import AsyncPostalcodeResource

        return AsyncPostalcodeResource(self)

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        from .resources.lookup import AsyncLookupResource

        return AsyncLookupResource(self)

    @cached_property
    def areas(self) -> AsyncAreasResource:
        from .resources.areas import AsyncAreasResource

        return AsyncAreasResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncNextbillionSDKWithRawResponse:
        return AsyncNextbillionSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNextbillionSDKWithStreamedResponse:
        return AsyncNextbillionSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key,
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class NextbillionSDKWithRawResponse:
    _client: NextbillionSDK

    def __init__(self, client: NextbillionSDK) -> None:
        self._client = client

    @cached_property
    def fleetify(self) -> fleetify.FleetifyResourceWithRawResponse:
        from .resources.fleetify import FleetifyResourceWithRawResponse

        return FleetifyResourceWithRawResponse(self._client.fleetify)

    @cached_property
    def skynet(self) -> skynet.SkynetResourceWithRawResponse:
        from .resources.skynet import SkynetResourceWithRawResponse

        return SkynetResourceWithRawResponse(self._client.skynet)

    @cached_property
    def geocode(self) -> geocode.GeocodeResourceWithRawResponse:
        from .resources.geocode import GeocodeResourceWithRawResponse

        return GeocodeResourceWithRawResponse(self._client.geocode)

    @cached_property
    def optimization(self) -> optimization.OptimizationResourceWithRawResponse:
        from .resources.optimization import OptimizationResourceWithRawResponse

        return OptimizationResourceWithRawResponse(self._client.optimization)

    @cached_property
    def geofence(self) -> geofence.GeofenceResourceWithRawResponse:
        from .resources.geofence import GeofenceResourceWithRawResponse

        return GeofenceResourceWithRawResponse(self._client.geofence)

    @cached_property
    def discover(self) -> discover.DiscoverResourceWithRawResponse:
        from .resources.discover import DiscoverResourceWithRawResponse

        return DiscoverResourceWithRawResponse(self._client.discover)

    @cached_property
    def browse(self) -> browse.BrowseResourceWithRawResponse:
        from .resources.browse import BrowseResourceWithRawResponse

        return BrowseResourceWithRawResponse(self._client.browse)

    @cached_property
    def mdm(self) -> mdm.MdmResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import MdmResourceWithRawResponse

        return MdmResourceWithRawResponse(self._client.mdm)

    @cached_property
    def isochrone(self) -> isochrone.IsochroneResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import IsochroneResourceWithRawResponse

        return IsochroneResourceWithRawResponse(self._client.isochrone)

    @cached_property
    def restrictions(self) -> restrictions.RestrictionsResourceWithRawResponse:
        from .resources.restrictions import RestrictionsResourceWithRawResponse

        return RestrictionsResourceWithRawResponse(self._client.restrictions)

    @cached_property
    def restrictions_items(self) -> restrictions_items.RestrictionsItemsResourceWithRawResponse:
        from .resources.restrictions_items import RestrictionsItemsResourceWithRawResponse

        return RestrictionsItemsResourceWithRawResponse(self._client.restrictions_items)

    @cached_property
    def distance_matrix(self) -> distance_matrix.DistanceMatrixResourceWithRawResponse:
        from .resources.distance_matrix import DistanceMatrixResourceWithRawResponse

        return DistanceMatrixResourceWithRawResponse(self._client.distance_matrix)

    @cached_property
    def autocomplete(self) -> autocomplete.AutocompleteResourceWithRawResponse:
        from .resources.autocomplete import AutocompleteResourceWithRawResponse

        return AutocompleteResourceWithRawResponse(self._client.autocomplete)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import NavigationResourceWithRawResponse

        return NavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def map(self) -> map.MapResourceWithRawResponse:
        from .resources.map import MapResourceWithRawResponse

        return MapResourceWithRawResponse(self._client.map)

    @cached_property
    def autosuggest(self) -> autosuggest.AutosuggestResourceWithRawResponse:
        from .resources.autosuggest import AutosuggestResourceWithRawResponse

        return AutosuggestResourceWithRawResponse(self._client.autosuggest)

    @cached_property
    def directions(self) -> directions.DirectionsResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import DirectionsResourceWithRawResponse

        return DirectionsResourceWithRawResponse(self._client.directions)

    @cached_property
    def batch(self) -> batch.BatchResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import BatchResourceWithRawResponse

        return BatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def multigeocode(self) -> multigeocode.MultigeocodeResourceWithRawResponse:
        from .resources.multigeocode import MultigeocodeResourceWithRawResponse

        return MultigeocodeResourceWithRawResponse(self._client.multigeocode)

    @cached_property
    def revgeocode(self) -> revgeocode.RevgeocodeResourceWithRawResponse:
        from .resources.revgeocode import RevgeocodeResourceWithRawResponse

        return RevgeocodeResourceWithRawResponse(self._client.revgeocode)

    @cached_property
    def route_report(self) -> route_report.RouteReportResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import RouteReportResourceWithRawResponse

        return RouteReportResourceWithRawResponse(self._client.route_report)

    @cached_property
    def snap_to_roads(self) -> snap_to_roads.SnapToRoadsResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import SnapToRoadsResourceWithRawResponse

        return SnapToRoadsResourceWithRawResponse(self._client.snap_to_roads)

    @cached_property
    def postalcode(self) -> postalcode.PostalcodeResourceWithRawResponse:
        from .resources.postalcode import PostalcodeResourceWithRawResponse

        return PostalcodeResourceWithRawResponse(self._client.postalcode)

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithRawResponse:
        from .resources.lookup import LookupResourceWithRawResponse

        return LookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def areas(self) -> areas.AreasResourceWithRawResponse:
        from .resources.areas import AreasResourceWithRawResponse

        return AreasResourceWithRawResponse(self._client.areas)


class AsyncNextbillionSDKWithRawResponse:
    _client: AsyncNextbillionSDK

    def __init__(self, client: AsyncNextbillionSDK) -> None:
        self._client = client

    @cached_property
    def fleetify(self) -> fleetify.AsyncFleetifyResourceWithRawResponse:
        from .resources.fleetify import AsyncFleetifyResourceWithRawResponse

        return AsyncFleetifyResourceWithRawResponse(self._client.fleetify)

    @cached_property
    def skynet(self) -> skynet.AsyncSkynetResourceWithRawResponse:
        from .resources.skynet import AsyncSkynetResourceWithRawResponse

        return AsyncSkynetResourceWithRawResponse(self._client.skynet)

    @cached_property
    def geocode(self) -> geocode.AsyncGeocodeResourceWithRawResponse:
        from .resources.geocode import AsyncGeocodeResourceWithRawResponse

        return AsyncGeocodeResourceWithRawResponse(self._client.geocode)

    @cached_property
    def optimization(self) -> optimization.AsyncOptimizationResourceWithRawResponse:
        from .resources.optimization import AsyncOptimizationResourceWithRawResponse

        return AsyncOptimizationResourceWithRawResponse(self._client.optimization)

    @cached_property
    def geofence(self) -> geofence.AsyncGeofenceResourceWithRawResponse:
        from .resources.geofence import AsyncGeofenceResourceWithRawResponse

        return AsyncGeofenceResourceWithRawResponse(self._client.geofence)

    @cached_property
    def discover(self) -> discover.AsyncDiscoverResourceWithRawResponse:
        from .resources.discover import AsyncDiscoverResourceWithRawResponse

        return AsyncDiscoverResourceWithRawResponse(self._client.discover)

    @cached_property
    def browse(self) -> browse.AsyncBrowseResourceWithRawResponse:
        from .resources.browse import AsyncBrowseResourceWithRawResponse

        return AsyncBrowseResourceWithRawResponse(self._client.browse)

    @cached_property
    def mdm(self) -> mdm.AsyncMdmResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import AsyncMdmResourceWithRawResponse

        return AsyncMdmResourceWithRawResponse(self._client.mdm)

    @cached_property
    def isochrone(self) -> isochrone.AsyncIsochroneResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import AsyncIsochroneResourceWithRawResponse

        return AsyncIsochroneResourceWithRawResponse(self._client.isochrone)

    @cached_property
    def restrictions(self) -> restrictions.AsyncRestrictionsResourceWithRawResponse:
        from .resources.restrictions import AsyncRestrictionsResourceWithRawResponse

        return AsyncRestrictionsResourceWithRawResponse(self._client.restrictions)

    @cached_property
    def restrictions_items(self) -> restrictions_items.AsyncRestrictionsItemsResourceWithRawResponse:
        from .resources.restrictions_items import AsyncRestrictionsItemsResourceWithRawResponse

        return AsyncRestrictionsItemsResourceWithRawResponse(self._client.restrictions_items)

    @cached_property
    def distance_matrix(self) -> distance_matrix.AsyncDistanceMatrixResourceWithRawResponse:
        from .resources.distance_matrix import AsyncDistanceMatrixResourceWithRawResponse

        return AsyncDistanceMatrixResourceWithRawResponse(self._client.distance_matrix)

    @cached_property
    def autocomplete(self) -> autocomplete.AsyncAutocompleteResourceWithRawResponse:
        from .resources.autocomplete import AsyncAutocompleteResourceWithRawResponse

        return AsyncAutocompleteResourceWithRawResponse(self._client.autocomplete)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import AsyncNavigationResourceWithRawResponse

        return AsyncNavigationResourceWithRawResponse(self._client.navigation)

    @cached_property
    def map(self) -> map.AsyncMapResourceWithRawResponse:
        from .resources.map import AsyncMapResourceWithRawResponse

        return AsyncMapResourceWithRawResponse(self._client.map)

    @cached_property
    def autosuggest(self) -> autosuggest.AsyncAutosuggestResourceWithRawResponse:
        from .resources.autosuggest import AsyncAutosuggestResourceWithRawResponse

        return AsyncAutosuggestResourceWithRawResponse(self._client.autosuggest)

    @cached_property
    def directions(self) -> directions.AsyncDirectionsResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import AsyncDirectionsResourceWithRawResponse

        return AsyncDirectionsResourceWithRawResponse(self._client.directions)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import AsyncBatchResourceWithRawResponse

        return AsyncBatchResourceWithRawResponse(self._client.batch)

    @cached_property
    def multigeocode(self) -> multigeocode.AsyncMultigeocodeResourceWithRawResponse:
        from .resources.multigeocode import AsyncMultigeocodeResourceWithRawResponse

        return AsyncMultigeocodeResourceWithRawResponse(self._client.multigeocode)

    @cached_property
    def revgeocode(self) -> revgeocode.AsyncRevgeocodeResourceWithRawResponse:
        from .resources.revgeocode import AsyncRevgeocodeResourceWithRawResponse

        return AsyncRevgeocodeResourceWithRawResponse(self._client.revgeocode)

    @cached_property
    def route_report(self) -> route_report.AsyncRouteReportResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import AsyncRouteReportResourceWithRawResponse

        return AsyncRouteReportResourceWithRawResponse(self._client.route_report)

    @cached_property
    def snap_to_roads(self) -> snap_to_roads.AsyncSnapToRoadsResourceWithRawResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import AsyncSnapToRoadsResourceWithRawResponse

        return AsyncSnapToRoadsResourceWithRawResponse(self._client.snap_to_roads)

    @cached_property
    def postalcode(self) -> postalcode.AsyncPostalcodeResourceWithRawResponse:
        from .resources.postalcode import AsyncPostalcodeResourceWithRawResponse

        return AsyncPostalcodeResourceWithRawResponse(self._client.postalcode)

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithRawResponse:
        from .resources.lookup import AsyncLookupResourceWithRawResponse

        return AsyncLookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def areas(self) -> areas.AsyncAreasResourceWithRawResponse:
        from .resources.areas import AsyncAreasResourceWithRawResponse

        return AsyncAreasResourceWithRawResponse(self._client.areas)


class NextbillionSDKWithStreamedResponse:
    _client: NextbillionSDK

    def __init__(self, client: NextbillionSDK) -> None:
        self._client = client

    @cached_property
    def fleetify(self) -> fleetify.FleetifyResourceWithStreamingResponse:
        from .resources.fleetify import FleetifyResourceWithStreamingResponse

        return FleetifyResourceWithStreamingResponse(self._client.fleetify)

    @cached_property
    def skynet(self) -> skynet.SkynetResourceWithStreamingResponse:
        from .resources.skynet import SkynetResourceWithStreamingResponse

        return SkynetResourceWithStreamingResponse(self._client.skynet)

    @cached_property
    def geocode(self) -> geocode.GeocodeResourceWithStreamingResponse:
        from .resources.geocode import GeocodeResourceWithStreamingResponse

        return GeocodeResourceWithStreamingResponse(self._client.geocode)

    @cached_property
    def optimization(self) -> optimization.OptimizationResourceWithStreamingResponse:
        from .resources.optimization import OptimizationResourceWithStreamingResponse

        return OptimizationResourceWithStreamingResponse(self._client.optimization)

    @cached_property
    def geofence(self) -> geofence.GeofenceResourceWithStreamingResponse:
        from .resources.geofence import GeofenceResourceWithStreamingResponse

        return GeofenceResourceWithStreamingResponse(self._client.geofence)

    @cached_property
    def discover(self) -> discover.DiscoverResourceWithStreamingResponse:
        from .resources.discover import DiscoverResourceWithStreamingResponse

        return DiscoverResourceWithStreamingResponse(self._client.discover)

    @cached_property
    def browse(self) -> browse.BrowseResourceWithStreamingResponse:
        from .resources.browse import BrowseResourceWithStreamingResponse

        return BrowseResourceWithStreamingResponse(self._client.browse)

    @cached_property
    def mdm(self) -> mdm.MdmResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import MdmResourceWithStreamingResponse

        return MdmResourceWithStreamingResponse(self._client.mdm)

    @cached_property
    def isochrone(self) -> isochrone.IsochroneResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import IsochroneResourceWithStreamingResponse

        return IsochroneResourceWithStreamingResponse(self._client.isochrone)

    @cached_property
    def restrictions(self) -> restrictions.RestrictionsResourceWithStreamingResponse:
        from .resources.restrictions import RestrictionsResourceWithStreamingResponse

        return RestrictionsResourceWithStreamingResponse(self._client.restrictions)

    @cached_property
    def restrictions_items(self) -> restrictions_items.RestrictionsItemsResourceWithStreamingResponse:
        from .resources.restrictions_items import RestrictionsItemsResourceWithStreamingResponse

        return RestrictionsItemsResourceWithStreamingResponse(self._client.restrictions_items)

    @cached_property
    def distance_matrix(self) -> distance_matrix.DistanceMatrixResourceWithStreamingResponse:
        from .resources.distance_matrix import DistanceMatrixResourceWithStreamingResponse

        return DistanceMatrixResourceWithStreamingResponse(self._client.distance_matrix)

    @cached_property
    def autocomplete(self) -> autocomplete.AutocompleteResourceWithStreamingResponse:
        from .resources.autocomplete import AutocompleteResourceWithStreamingResponse

        return AutocompleteResourceWithStreamingResponse(self._client.autocomplete)

    @cached_property
    def navigation(self) -> navigation.NavigationResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import NavigationResourceWithStreamingResponse

        return NavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def map(self) -> map.MapResourceWithStreamingResponse:
        from .resources.map import MapResourceWithStreamingResponse

        return MapResourceWithStreamingResponse(self._client.map)

    @cached_property
    def autosuggest(self) -> autosuggest.AutosuggestResourceWithStreamingResponse:
        from .resources.autosuggest import AutosuggestResourceWithStreamingResponse

        return AutosuggestResourceWithStreamingResponse(self._client.autosuggest)

    @cached_property
    def directions(self) -> directions.DirectionsResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import DirectionsResourceWithStreamingResponse

        return DirectionsResourceWithStreamingResponse(self._client.directions)

    @cached_property
    def batch(self) -> batch.BatchResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import BatchResourceWithStreamingResponse

        return BatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def multigeocode(self) -> multigeocode.MultigeocodeResourceWithStreamingResponse:
        from .resources.multigeocode import MultigeocodeResourceWithStreamingResponse

        return MultigeocodeResourceWithStreamingResponse(self._client.multigeocode)

    @cached_property
    def revgeocode(self) -> revgeocode.RevgeocodeResourceWithStreamingResponse:
        from .resources.revgeocode import RevgeocodeResourceWithStreamingResponse

        return RevgeocodeResourceWithStreamingResponse(self._client.revgeocode)

    @cached_property
    def route_report(self) -> route_report.RouteReportResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import RouteReportResourceWithStreamingResponse

        return RouteReportResourceWithStreamingResponse(self._client.route_report)

    @cached_property
    def snap_to_roads(self) -> snap_to_roads.SnapToRoadsResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import SnapToRoadsResourceWithStreamingResponse

        return SnapToRoadsResourceWithStreamingResponse(self._client.snap_to_roads)

    @cached_property
    def postalcode(self) -> postalcode.PostalcodeResourceWithStreamingResponse:
        from .resources.postalcode import PostalcodeResourceWithStreamingResponse

        return PostalcodeResourceWithStreamingResponse(self._client.postalcode)

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithStreamingResponse:
        from .resources.lookup import LookupResourceWithStreamingResponse

        return LookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def areas(self) -> areas.AreasResourceWithStreamingResponse:
        from .resources.areas import AreasResourceWithStreamingResponse

        return AreasResourceWithStreamingResponse(self._client.areas)


class AsyncNextbillionSDKWithStreamedResponse:
    _client: AsyncNextbillionSDK

    def __init__(self, client: AsyncNextbillionSDK) -> None:
        self._client = client

    @cached_property
    def fleetify(self) -> fleetify.AsyncFleetifyResourceWithStreamingResponse:
        from .resources.fleetify import AsyncFleetifyResourceWithStreamingResponse

        return AsyncFleetifyResourceWithStreamingResponse(self._client.fleetify)

    @cached_property
    def skynet(self) -> skynet.AsyncSkynetResourceWithStreamingResponse:
        from .resources.skynet import AsyncSkynetResourceWithStreamingResponse

        return AsyncSkynetResourceWithStreamingResponse(self._client.skynet)

    @cached_property
    def geocode(self) -> geocode.AsyncGeocodeResourceWithStreamingResponse:
        from .resources.geocode import AsyncGeocodeResourceWithStreamingResponse

        return AsyncGeocodeResourceWithStreamingResponse(self._client.geocode)

    @cached_property
    def optimization(self) -> optimization.AsyncOptimizationResourceWithStreamingResponse:
        from .resources.optimization import AsyncOptimizationResourceWithStreamingResponse

        return AsyncOptimizationResourceWithStreamingResponse(self._client.optimization)

    @cached_property
    def geofence(self) -> geofence.AsyncGeofenceResourceWithStreamingResponse:
        from .resources.geofence import AsyncGeofenceResourceWithStreamingResponse

        return AsyncGeofenceResourceWithStreamingResponse(self._client.geofence)

    @cached_property
    def discover(self) -> discover.AsyncDiscoverResourceWithStreamingResponse:
        from .resources.discover import AsyncDiscoverResourceWithStreamingResponse

        return AsyncDiscoverResourceWithStreamingResponse(self._client.discover)

    @cached_property
    def browse(self) -> browse.AsyncBrowseResourceWithStreamingResponse:
        from .resources.browse import AsyncBrowseResourceWithStreamingResponse

        return AsyncBrowseResourceWithStreamingResponse(self._client.browse)

    @cached_property
    def mdm(self) -> mdm.AsyncMdmResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.mdm import AsyncMdmResourceWithStreamingResponse

        return AsyncMdmResourceWithStreamingResponse(self._client.mdm)

    @cached_property
    def isochrone(self) -> isochrone.AsyncIsochroneResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.isochrone import AsyncIsochroneResourceWithStreamingResponse

        return AsyncIsochroneResourceWithStreamingResponse(self._client.isochrone)

    @cached_property
    def restrictions(self) -> restrictions.AsyncRestrictionsResourceWithStreamingResponse:
        from .resources.restrictions import AsyncRestrictionsResourceWithStreamingResponse

        return AsyncRestrictionsResourceWithStreamingResponse(self._client.restrictions)

    @cached_property
    def restrictions_items(self) -> restrictions_items.AsyncRestrictionsItemsResourceWithStreamingResponse:
        from .resources.restrictions_items import AsyncRestrictionsItemsResourceWithStreamingResponse

        return AsyncRestrictionsItemsResourceWithStreamingResponse(self._client.restrictions_items)

    @cached_property
    def distance_matrix(self) -> distance_matrix.AsyncDistanceMatrixResourceWithStreamingResponse:
        from .resources.distance_matrix import AsyncDistanceMatrixResourceWithStreamingResponse

        return AsyncDistanceMatrixResourceWithStreamingResponse(self._client.distance_matrix)

    @cached_property
    def autocomplete(self) -> autocomplete.AsyncAutocompleteResourceWithStreamingResponse:
        from .resources.autocomplete import AsyncAutocompleteResourceWithStreamingResponse

        return AsyncAutocompleteResourceWithStreamingResponse(self._client.autocomplete)

    @cached_property
    def navigation(self) -> navigation.AsyncNavigationResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.navigation import AsyncNavigationResourceWithStreamingResponse

        return AsyncNavigationResourceWithStreamingResponse(self._client.navigation)

    @cached_property
    def map(self) -> map.AsyncMapResourceWithStreamingResponse:
        from .resources.map import AsyncMapResourceWithStreamingResponse

        return AsyncMapResourceWithStreamingResponse(self._client.map)

    @cached_property
    def autosuggest(self) -> autosuggest.AsyncAutosuggestResourceWithStreamingResponse:
        from .resources.autosuggest import AsyncAutosuggestResourceWithStreamingResponse

        return AsyncAutosuggestResourceWithStreamingResponse(self._client.autosuggest)

    @cached_property
    def directions(self) -> directions.AsyncDirectionsResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.directions import AsyncDirectionsResourceWithStreamingResponse

        return AsyncDirectionsResourceWithStreamingResponse(self._client.directions)

    @cached_property
    def batch(self) -> batch.AsyncBatchResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.batch import AsyncBatchResourceWithStreamingResponse

        return AsyncBatchResourceWithStreamingResponse(self._client.batch)

    @cached_property
    def multigeocode(self) -> multigeocode.AsyncMultigeocodeResourceWithStreamingResponse:
        from .resources.multigeocode import AsyncMultigeocodeResourceWithStreamingResponse

        return AsyncMultigeocodeResourceWithStreamingResponse(self._client.multigeocode)

    @cached_property
    def revgeocode(self) -> revgeocode.AsyncRevgeocodeResourceWithStreamingResponse:
        from .resources.revgeocode import AsyncRevgeocodeResourceWithStreamingResponse

        return AsyncRevgeocodeResourceWithStreamingResponse(self._client.revgeocode)

    @cached_property
    def route_report(self) -> route_report.AsyncRouteReportResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.route_report import AsyncRouteReportResourceWithStreamingResponse

        return AsyncRouteReportResourceWithStreamingResponse(self._client.route_report)

    @cached_property
    def snap_to_roads(self) -> snap_to_roads.AsyncSnapToRoadsResourceWithStreamingResponse:
        """<p>Get travel time and find optimal routes.

        Add guided navigation and gain trip data insights.</p>
        """
        from .resources.snap_to_roads import AsyncSnapToRoadsResourceWithStreamingResponse

        return AsyncSnapToRoadsResourceWithStreamingResponse(self._client.snap_to_roads)

    @cached_property
    def postalcode(self) -> postalcode.AsyncPostalcodeResourceWithStreamingResponse:
        from .resources.postalcode import AsyncPostalcodeResourceWithStreamingResponse

        return AsyncPostalcodeResourceWithStreamingResponse(self._client.postalcode)

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithStreamingResponse:
        from .resources.lookup import AsyncLookupResourceWithStreamingResponse

        return AsyncLookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def areas(self) -> areas.AsyncAreasResourceWithStreamingResponse:
        from .resources.areas import AsyncAreasResourceWithStreamingResponse

        return AsyncAreasResourceWithStreamingResponse(self._client.areas)


Client = NextbillionSDK

AsyncClient = AsyncNextbillionSDK
